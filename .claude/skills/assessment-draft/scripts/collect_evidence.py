#!/usr/bin/env python3
"""Collect read-only evidence from a repository and its git history for the assessment-draft skill.

Usage: collect_evidence.py REPO [--author NAME_OR_EMAIL] [--since YYYY-MM-DD] [--until YYYY-MM-DD]
                           [--out DIR] [--max-files N]
Writes evidence.json and evidence.md to DIR (default ./assessment-draft/<repo name>/).
Standard library only. Never modifies the repository and never touches the network.
"""
from __future__ import annotations
import argparse, json, os, re, statistics, subprocess, sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

SKIP_DIRS = {'node_modules', 'dist', 'build', '.next', '.nuxt', 'out', 'coverage', 'vendor', '.turbo', '.cache', 'storybook-static', '.vitepress/cache', '.vitepress/dist', 'target', '.venv', '__pycache__'}
GENERATED = re.compile(r'(package-lock\.json|pnpm-lock\.yaml|yarn\.lock|bun\.lockb|\.snap$|/generated/|\.min\.(js|css)$|\.map$)')
TEXT_EXT = {'.js', '.jsx', '.mjs', '.cjs', '.ts', '.tsx', '.mts', '.cts', '.vue', '.svelte', '.astro', '.html', '.css', '.scss', '.sass', '.less', '.json', '.md', '.mdx', '.yml', '.yaml', '.toml', '.env', '.txt', '.sh', '.py', '.rb', '.go', '.java', '.kt', '.php', '.cs', '.xml', '.graphql', '.gql'}
MAX_CONTENT_BYTES = 300_000
DOC_EXT = {'.md', '.mdx', '.txt'}

# --- source-content signals: name -> (regex, skill ids, description) -------------------------------
SIGNALS = {
 'use_client': (r"""['"]use client['"]""", ['nextjs.rendering'], "'use client' 指定"),
 'use_server': (r"""['"]use server['"]""", ['nextjs.rendering'], "'use server'（Server Actions）"),
 'revalidate': (r'\brevalidate(Path|Tag)?\b|\bunstable_cache\b|\bcache:\s*[\'"](no-store|force-cache)', ['nextjs.rendering', 'web.basic'], 'キャッシュ・再検証の指定'),
 'metadata': (r'\bgenerateMetadata\b|export const metadata\b|<meta\b|<title>', ['web.seo'], 'メタデータ・タイトルの設定'),
 'seo_files': (r'robots\.txt|sitemap', ['web.seo'], 'robots／sitemap への言及'),
 'next_image': (r'next/image|next/font', ['web.performance'], 'next/image・next/font'),
 'dynamic_import': (r'next/dynamic|React\.lazy\(|\bimport\((?![^)]*\.json)', ['web.performance'], '動的インポート'),
 'web_vitals': (r'web-vitals|reportWebVitals|useReportWebVitals', ['web.performance'], 'Web Vitals の計測'),
 'suspense': (r'<Suspense\b|\bloading\.tsx\b', ['nextjs.rendering', 'web.performance'], 'Suspense／段階的な表示'),
 'error_boundary': (r'ErrorBoundary|\berror\.tsx\b|notFound\(\)', ['nextjs.routing', 'react.basic'], 'エラー境界・404 の扱い'),
 'aria': (r'\baria-[a-z]+=|\brole=["\']', ['web.accessibility', 'html.semantic'], 'ARIA 属性・role'),
 'alt_lang': (r'\balt=|<html[^>]*\blang=', ['web.accessibility', 'html.basic'], 'alt／lang 属性'),
 'semantic': (r'<(main|nav|header|footer|article|section|aside)\b', ['html.semantic'], 'セマンティック要素'),
 'forms': (r'<form\b|<label\b|htmlFor=|<fieldset\b', ['html.basic', 'react.form'], 'フォーム要素'),
 'rhf': (r'react-hook-form|\buseForm\(', ['react.form'], 'react-hook-form'),
 'schema': (r"""from ['"](zod|yup|valibot)['"]|\bz\.object\(""", ['frontend.validation'], 'スキーマ検証（Zod 等）'),
 'fetch': (r'\bfetch\(', ['frontend.api-integration', 'web.basic'], 'fetch の利用'),
 'axios': (r'\baxios\b|\bky\b', ['frontend.api-integration'], 'axios／ky'),
 'query': (r'@tanstack/react-query|\buseQuery\(|\buseMutation\(|\buseSWR\(', ['frontend.api-integration', 'react.state-management'], 'サーバー状態（TanStack Query／SWR）'),
 'openapi': (r'orval|openapi-zod-client|openapi-typescript|swagger', ['frontend.api-integration'], 'OpenAPI からの生成'),
 'msw': (r"""from ['"]msw""", ['test.integration', 'frontend.api-integration'], 'MSW'),
 'state_lib': (r'\bzustand\b|@reduxjs|createSlice\(|\bjotai\b|\bvaltio\b', ['react.state-management'], '状態管理ライブラリ'),
 'context_reducer': (r'createContext\(|useReducer\(', ['react.state-management'], 'Context／useReducer'),
 'async': (r'\bawait\b', ['javascript.async'], 'async/await'),
 'promise_all': (r'Promise\.(all|allSettled|race|any)\(', ['javascript.async'], '並列処理'),
 'abort_retry': (r'AbortController|\bretry\b|\bbackoff\b|\btimeout\b', ['javascript.async', 'web.basic'], 'キャンセル・再試行・タイムアウト'),
 'dom': (r'document\.(querySelector|getElementById|createElement)|addEventListener\(|\.focus\(\)', ['javascript.dom'], 'DOM・イベント操作'),
 'cookies': (r'\bcookies\(\)|document\.cookie|Set-Cookie|\bsameSite\b|\bhttpOnly\b', ['web.basic', 'web.security'], 'Cookie の扱い'),
 'cache_control': (r'Cache-Control|stale-while-revalidate|s-maxage|\bETag\b', ['web.basic', 'web.performance'], 'HTTP キャッシュ制御'),
 'csp': (r'Content-Security-Policy|X-Frame-Options|Strict-Transport-Security|Permissions-Policy', ['web.security'], 'セキュリティヘッダー'),
 'sanitize': (r'DOMPurify|sanitize(Html)?\(', ['web.security'], 'サニタイズ'),
 'dangerous': (r'dangerouslySetInnerHTML|\binnerHTML\s*=|\beval\(|new Function\(', ['web.security'], '危険な出力・eval'),
 'auth': (r'\bnext-auth\b|\bauth\.js\b|Authorization:|\bjwt\b|\bauthorize\(', ['web.security'], '認証・認可の扱い'),
 'testing_library': (r'@testing-library', ['test.component'], 'Testing Library'),
 'axe': (r'vitest-axe|jest-axe|toHaveNoViolations|@axe-core', ['web.accessibility', 'test.component'], 'axe による検査'),
 'playwright': (r'@playwright/test|\bcypress\b', ['test.e2e'], 'Playwright／Cypress'),
 'storybook': (r'@storybook/|satisfies Meta<|: Meta<', ['storybook.basic'], 'Storybook'),
 'tailwind': (r'className="[^"]*\b(sm|md|lg|xl|2xl):|@apply\b|tailwind', ['frontend.styling', 'css.responsive'], 'Tailwind のクラス・設定'),
 'media_query': (r'@media\b|@container\b|\bclamp\(|\bminmax\(', ['css.responsive'], 'メディアクエリ・流動的な値'),
 'layout': (r'display:\s*(grid|flex)|grid-template|flex-direction', ['css.basic', 'css.responsive'], 'Grid／Flexbox'),
 'css_vars': (r'--[a-z][a-z0-9-]*\s*:|var\(--', ['frontend.styling', 'css.basic'], 'CSS 変数・トークン'),
 'cva_shadcn': (r'class-variance-authority|\bcva\(|components/ui/', ['frontend.styling', 'react.component-design'], 'cva／shadcn/ui'),
 'i18n': (r'next-intl|i18next|useTranslations\(|\bt\(["\']', ['nextjs.routing'], '多言語対応'),
 'monitoring': (r'@sentry/|datadog|newrelic|\bopentelemetry\b', [], '監視・エラー収集'),
 'analytics': (r'\bgtag\(|googletagmanager|@vercel/analytics|posthog|amplitude|segment', [], '解析ツール'),
 'feature_flags': (r'launchdarkly|unleash|flagsmith|featureFlag', [], 'フィーチャーフラグ'),
 'ts_escape': (r'@ts-ignore|@ts-expect-error|:\s*any\b|\bas any\b', ['typescript.basic'], 'any／@ts-ignore（多いほど弱い根拠）'),
 'lint_disable': (r'eslint-disable', ['frontend.quality'], 'eslint-disable'),
 'console_log': (r'console\.log\(', ['frontend.quality'], 'console.log'),
 'todo': (r'\b(TODO|FIXME|HACK)\b', ['frontend.quality'], 'TODO／FIXME'),
}
SECRET_PATTERNS = {
 'AWS access key': r'\bAKIA[0-9A-Z]{16}\b',
 'private key block': r'-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
 'generic secret assignment': r'(?i)\b(api[_-]?key|secret|token|password|passwd|client_secret)\b\s*[:=]\s*["\'][A-Za-z0-9_\-\.=+/]{16,}["\']',
 'GitHub token': r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',
 'Slack token': r'\bxox[baprs]-[A-Za-z0-9-]{10,}\b',
 'Google API key': r'\bAIza[0-9A-Za-z\-_]{35}\b',
}
SECRET_SKIP = re.compile(r'(\.example$|\.sample$|\.md$|\.mdx$|lock\.(json|yaml)$|yarn\.lock$|/test|/__tests__/|/fixtures?/|\.test\.|\.spec\.|\.stories\.)')

KNOWN_DEPS = {
 'react': 'React', 'react-dom': 'React', 'next': 'Next.js', 'vue': 'Vue', 'nuxt': 'Nuxt', 'svelte': 'Svelte', '@angular/core': 'Angular', 'astro': 'Astro', 'solid-js': 'Solid',
 'typescript': 'TypeScript', 'vite': 'Vite', 'webpack': 'webpack', 'turbo': 'Turborepo', 'nx': 'Nx',
 'tailwindcss': 'Tailwind CSS', 'sass': 'Sass', 'styled-components': 'styled-components', '@emotion/react': 'Emotion', 'class-variance-authority': 'cva', 'style-dictionary': 'Style Dictionary',
 '@radix-ui/react-dialog': 'Radix UI', '@headlessui/react': 'Headless UI', '@mui/material': 'MUI', 'antd': 'Ant Design', '@chakra-ui/react': 'Chakra UI',
 '@tanstack/react-query': 'TanStack Query', 'swr': 'SWR', 'zustand': 'Zustand', '@reduxjs/toolkit': 'Redux Toolkit', 'jotai': 'Jotai', 'valtio': 'Valtio',
 'react-hook-form': 'react-hook-form', 'zod': 'Zod', 'yup': 'Yup', 'valibot': 'Valibot', 'axios': 'axios', 'ky': 'ky', 'orval': 'orval', 'openapi-zod-client': 'openapi-zod-client', 'openapi-typescript': 'openapi-typescript', 'msw': 'MSW',
 'next-intl': 'next-intl', 'i18next': 'i18next', 'react-i18next': 'react-i18next', 'sonner': 'Sonner', 'next-auth': 'NextAuth.js',
 'vitest': 'Vitest', 'jest': 'Jest', '@testing-library/react': 'Testing Library', 'vitest-axe': 'vitest-axe', 'jest-axe': 'jest-axe', '@playwright/test': 'Playwright', 'cypress': 'Cypress',
 'storybook': 'Storybook', '@storybook/react': 'Storybook', '@storybook/addon-a11y': 'Storybook a11y addon', '@storybook/addon-vitest': 'Storybook Vitest addon', '@storybook/experimental-addon-test': 'Storybook test addon', 'chromatic': 'Chromatic', 'storycap': 'storycap', 'reg-suit': 'reg-suit',
 'eslint': 'ESLint', 'prettier': 'Prettier', 'eslint-plugin-jsx-a11y': 'eslint-plugin-jsx-a11y', 'husky': 'husky', 'lint-staged': 'lint-staged', '@commitlint/cli': 'commitlint', 'biome': 'Biome', '@biomejs/biome': 'Biome',
 '@lhci/cli': 'Lighthouse CI', 'web-vitals': 'web-vitals', '@next/bundle-analyzer': 'Bundle Analyzer', 'dompurify': 'DOMPurify', '@sentry/nextjs': 'Sentry', '@sentry/react': 'Sentry', '@vercel/analytics': 'Vercel Analytics',
}
CI_KEYWORDS = {
 'lint': r'\b(eslint|lint|biome)\b', 'typecheck': r'\b(tsc|typecheck|type-check|vue-tsc)\b', 'unit tests': r'\b(vitest|jest|npm test|pnpm test|yarn test|test:unit)\b', 'build': r'\b(build)\b',
 'e2e': r'\b(playwright|cypress|e2e)\b', 'storybook': r'\b(storybook|chromatic|storycap|reg-suit)\b', 'accessibility': r'\b(axe|pa11y|a11y)\b', 'performance': r'\b(lighthouse|lhci|web-vitals|bundle)\b',
 'SAST': r'\b(codeql|semgrep|sonar)\b', 'dependency audit': r'\b(npm audit|pnpm audit|yarn audit|trivy|snyk|osv-scanner|dependency-review)\b', 'secret scan': r'\b(gitleaks|trufflehog|secret-scan)\b',
 'deploy': r'\b(deploy|vercel|netlify|pages|cloudfront|s3 sync|kubectl|helm)\b', 'scheduled run': r'^\s*schedule:', 'pull_request trigger': r'pull_request', 'environments': r'^\s*environment:', 'concurrency': r'^\s*concurrency:', 'cache': r'actions/cache|cache:\s*[\'"]?(npm|pnpm|yarn)', 'continue-on-error': r'continue-on-error:\s*true', 'sharding': r'--shard|shardIndex|matrix:',
}
CONFIG_FILES = [
 ('ESLint', r'(^|/)(eslint\.config\.(js|mjs|cjs|ts)|\.eslintrc(\.\w+)?)$'), ('Prettier', r'(^|/)(\.prettierrc(\.\w+)?|prettier\.config\.\w+)$'), ('Biome', r'(^|/)biome\.jsonc?$'),
 ('tsconfig', r'(^|/)tsconfig(\.\w+)?\.json$'), ('.editorconfig', r'(^|/)\.editorconfig$'), ('husky', r'(^|/)\.husky/'), ('lint-staged', r'(^|/)(\.lintstagedrc(\.\w+)?|lint-staged\.config\.\w+)$'), ('commitlint', r'(^|/)(commitlint\.config\.\w+|\.commitlintrc(\.\w+)?)$'),
 ('Vitest／Jest config', r'(^|/)(vitest|jest)\.config\.\w+$'), ('Playwright／Cypress config', r'(^|/)(playwright|cypress)\.config\.\w+$'), ('Storybook', r'(^|/)\.storybook/'), ('Tailwind config', r'(^|/)tailwind\.config\.\w+$'), ('PostCSS config', r'(^|/)postcss\.config\.\w+$'),
 ('Next.js config', r'(^|/)next\.config\.\w+$'), ('Vite config', r'(^|/)vite\.config\.\w+$'), ('.nvmrc／.node-version', r'(^|/)(\.nvmrc|\.node-version|\.tool-versions)$'), ('.env.example', r'(^|/)\.env(\.\w+)?\.(example|sample|template)$'),
 ('Dockerfile', r'(^|/)Dockerfile'), ('docker-compose', r'(^|/)(docker-)?compose\.ya?ml$'), ('Dev Container', r'(^|/)\.devcontainer/'), ('Vercel／Netlify config', r'(^|/)(vercel\.json|netlify\.toml)$'), ('IaC（Terraform／CDK）', r'(\.tf$|(^|/)cdk\.json$)'), ('Kubernetes manifests', r'(^|/)(k8s|kubernetes|helm)/'),
 ('Renovate／Dependabot', r'(^|/)(renovate\.json5?|\.renovaterc(\.json)?|\.github/dependabot\.ya?ml)$'), ('CODEOWNERS', r'(^|/)CODEOWNERS$'), ('PR template', r'(?i)(^|/)pull_request_template\.md$'), ('Issue templates', r'(^|/)\.github/ISSUE_TEMPLATE/'),
 ('README', r'^README(\.\w+)?$'), ('CONTRIBUTING', r'(^|/)CONTRIBUTING(\.\w+)?$'), ('CHANGELOG', r'(^|/)CHANGELOG(\.\w+)?$'), ('LICENSE', r'(^|/)LICENSE'), ('SECURITY.md', r'(^|/)SECURITY\.md$'), ('docs ディレクトリ', r'^docs?/'), ('ADR／設計記録', r'(?i)(^|/)(adr|adrs|decisions|architecture)/'), ('RUNBOOK／インシデント手順らしきファイル（要確認）', r'(?i)(^|/)(runbook|incident|postmortem|on-?call)'),
 ('Lighthouse CI config', r'(^|/)lighthouserc(\.\w+)?$'), ('Sentry config', r'(^|/)sentry\.\w+\.config\.\w+$'), ('OpenAPI 定義', r'(?i)(^|/)(openapi|swagger)[^/]*\.(ya?ml|json)$'), ('MSW handlers', r'(^|/)(mocks?|msw)/'), ('locales（多言語）', r'(^|/)(locales?|messages|i18n)/'), ('robots.txt／sitemap', r'(^|/)(robots\.txt|sitemap[^/]*)$'), ('browserslist', r'(^|/)\.browserslistrc$'), ('codecov config', r'(^|/)(codecov\.ya?ml|\.codecov\.ya?ml)$'),
]
TEST_FILE = re.compile(r'(\.(test|spec)\.[cm]?[jt]sx?$|(^|/)__tests__/)')
E2E_FILE = re.compile(r'((^|/)(e2e|tests?/e2e|playwright|cypress)/.*\.[cm]?[jt]sx?$)')
STORY_FILE = re.compile(r'\.stories\.[cm]?[jt]sx?$|\.mdx$')
SOURCE_FILE = re.compile(r'\.(js|jsx|mjs|cjs|ts|tsx|vue|svelte|astro)$')
STYLE_FILE = re.compile(r'\.(css|scss|sass|less)$')
NEXT_ROUTE = re.compile(r'(^|/)app/.*/(page|layout|loading|error|not-found|template|route|default)\.[jt]sx?$|(^|/)app/(page|layout|loading|error|not-found)\.[jt]sx?$')

def skills_for_path(path: str) -> set[str]:
    s: set[str] = set(); p = path
    if GENERATED.search(p) or Path(p).suffix.lower() in DOC_EXT: return s  # prose describes tools; it is not evidence of using them
    if p.endswith('.html'): s |= {'html.basic', 'html.semantic'}
    if STYLE_FILE.search(p): s |= {'css.basic', 'css.responsive', 'frontend.styling'}
    if re.search(r'tailwind\.config|postcss\.config|/styles?/|/theme/|tokens?\.(json|css|ts)$', p): s.add('frontend.styling')
    if re.search(r'\.(js|jsx|mjs|cjs)$', p): s.add('javascript.basic')
    if re.search(r'\.(ts|tsx|mts|cts)$', p): s |= {'typescript.basic', 'javascript.basic'}
    if re.search(r'\.(tsx|jsx)$', p): s |= {'react.basic'}
    if re.search(r'(^|/)components?/', p) and SOURCE_FILE.search(p): s.add('react.component-design')
    if NEXT_ROUTE.search(p) or re.search(r'(^|/)middleware\.[jt]s$', p): s.add('nextjs.routing')
    if re.search(r'(^|/)(actions?|server)/', p) and SOURCE_FILE.search(p): s.add('nextjs.rendering')
    if re.search(r'(^|/)(store|stores|state)/', p): s.add('react.state-management')
    if re.search(r'(^|/)(api|services?|clients?|lib/http|queries)/', p) and SOURCE_FILE.search(p): s.add('frontend.api-integration')
    if re.search(r'(^|/)(forms?|validation|schemas?)/', p): s |= {'react.form', 'frontend.validation'}
    if STORY_FILE.search(p) and not p.endswith('.mdx'): s.add('storybook.basic')
    if re.search(r'(^|/)\.storybook/', p): s.add('storybook.basic')
    if E2E_FILE.search(p) or re.search(r'playwright\.config|cypress\.config', p): s.add('test.e2e')
    elif TEST_FILE.search(p):
        s.add('test.unit'); s.add('test.design')
        if re.search(r'\.(tsx|jsx)$', p) or '/components/' in p: s.add('test.component')
        if re.search(r'integration|/api/|msw', p): s.add('test.integration')
    if re.search(r'(^|/)(mocks?|msw)/', p): s.add('test.integration')
    if re.search(r'(^|/)(\.github/|\.gitlab-ci|CODEOWNERS|PULL_REQUEST_TEMPLATE|CONTRIBUTING)', p): s.add('git.collaboration')
    if re.search(r'(eslint|prettier|biome|tsconfig|vitest\.config|jest\.config|lint-staged|\.husky|commitlint|\.editorconfig)', p): s.add('frontend.quality')
    if re.search(r'lighthouserc|web-vitals|bundle-analyzer', p): s.add('web.performance')
    if re.search(r'(^|/)(auth|security|csp)', p) or re.search(r'middleware\.[jt]s$', p): s.add('web.security')
    if re.search(r'(^|/)(robots\.txt|sitemap)', p) or re.search(r'opengraph-image|twitter-image', p): s.add('web.seo')
    if re.search(r'(^|/)(locales?|messages|i18n)/', p): s.add('nextjs.routing')
    return s

def git(repo: Path, *args: str, check: bool = False) -> str:
    try:
        r = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, text=True, errors='replace')
        if check and r.returncode: raise RuntimeError(r.stderr.strip())
        return r.stdout
    except FileNotFoundError:
        sys.exit('git が見つかりません。')

def read_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_CONTENT_BYTES: return None
        return path.read_text(encoding='utf-8', errors='replace')
    except (OSError, UnicodeDecodeError): return None

def tracked_files(repo: Path) -> list[str]:
    out = git(repo, 'ls-files', '-z')
    files = [f for f in out.split('\0') if f]
    return [f for f in files if not any(part in SKIP_DIRS for part in f.split('/'))]

def load_json(path: Path):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception: return None

def collect_stack(repo: Path, files: list[str]) -> dict:
    stack = {'packages': [], 'tools': [], 'scripts': {}, 'package_manager': None, 'node': None, 'workspaces': []}
    pkg_files = [f for f in files if f.endswith('package.json') and f.count('/') <= 2]
    deps: dict[str, str] = {}
    for f in sorted(pkg_files, key=lambda x: x.count('/')):
        data = load_json(repo / f)
        if not isinstance(data, dict): continue
        stack['packages'].append({'path': f, 'name': data.get('name'), 'private': data.get('private')})
        for key in ('dependencies', 'devDependencies', 'peerDependencies'):
            for name, ver in (data.get(key) or {}).items(): deps.setdefault(name, str(ver))
        if f == 'package.json':
            stack['scripts'] = {k: str(v)[:120] for k, v in (data.get('scripts') or {}).items()}
            stack['node'] = (data.get('engines') or {}).get('node')
            if data.get('workspaces'): stack['workspaces'] = data['workspaces'] if isinstance(data['workspaces'], list) else list(data['workspaces'].get('packages', []))
    for lock, pm in (('pnpm-lock.yaml', 'pnpm'), ('yarn.lock', 'yarn'), ('package-lock.json', 'npm'), ('bun.lockb', 'bun'), ('bun.lock', 'bun')):
        if lock in files: stack['package_manager'] = pm; break
    for f in ('.nvmrc', '.node-version'):
        if f in files and not stack['node']:
            t = read_text(repo / f); stack['node'] = t.strip() if t else None
    stack['tools'] = sorted({KNOWN_DEPS[d] + (f' {deps[d]}' if d in ('react', 'next', 'vue', 'typescript', 'tailwindcss', 'vitest', 'storybook', '@playwright/test') else '') for d in deps if d in KNOWN_DEPS})
    stack['dependency_count'] = len(deps)
    stack['pnpm_workspace'] = 'pnpm-workspace.yaml' in files
    return stack

def collect_configs(files: list[str]) -> dict:
    found: dict[str, list[str]] = {}
    for label, pattern in CONFIG_FILES:
        rx = re.compile(pattern)
        hits = [f for f in files if rx.search(f)]
        if hits: found[label] = hits[:5]
    return found

def tsconfig_strict(repo: Path, files: list[str]) -> bool | None:
    for f in files:
        if re.search(r'(^|/)tsconfig\.json$', f):
            t = read_text(repo / f)
            if t is None: continue
            t = re.sub(r'//.*', '', t); t = re.sub(r'/\*.*?\*/', '', t, flags=re.S)
            return bool(re.search(r'"strict"\s*:\s*true', t))
    return None

def collect_ci(repo: Path, files: list[str]) -> list[dict]:
    ci_files = [f for f in files if re.search(r'(^|/)\.github/workflows/.*\.ya?ml$|^\.gitlab-ci\.ya?ml$|^\.circleci/config\.ya?ml$|^bitbucket-pipelines\.ya?ml$|^azure-pipelines\.ya?ml$|^Jenkinsfile$', f)]
    out = []
    for f in ci_files:
        t = read_text(repo / f) or ''
        name = re.search(r'^name:\s*(.+)$', t, re.M)
        hits = [k for k, rx in CI_KEYWORDS.items() if re.search(rx, t, re.M | re.I)]
        out.append({'path': f, 'name': name.group(1).strip().strip('"\'') if name else None, 'checks': hits})
    return out

def scan_contents(repo: Path, files: list[str]) -> tuple[dict, dict, list]:
    """Return (per-file signal hits, per-signal aggregate, secret findings)."""
    per_file: dict[str, dict[str, int]] = {}
    per_signal: dict[str, dict] = {k: {'files': 0, 'hits': 0, 'examples': []} for k in SIGNALS}
    secrets: list[dict] = []
    compiled = {k: re.compile(v[0], re.M) for k, v in SIGNALS.items()}
    secret_rx = {k: re.compile(v) for k, v in SECRET_PATTERNS.items()}
    for f in files:
        if GENERATED.search(f) or Path(f).suffix.lower() not in TEXT_EXT: continue
        t = read_text(repo / f)
        if t is None: continue
        hits = {}
        is_doc = Path(f).suffix.lower() in DOC_EXT  # prose files describe tools without using them: no code signals, secrets still checked
        for k, rx in (compiled.items() if not is_doc else ()):
            n = len(rx.findall(t))
            if n:
                hits[k] = n; agg = per_signal[k]; agg['files'] += 1; agg['hits'] += n
                if len(agg['examples']) < 3: agg['examples'].append(f)
        if hits: per_file[f] = hits
        if not SECRET_SKIP.search(f):
            for label, rx in secret_rx.items():
                for m in rx.finditer(t):
                    line = t.count('\n', 0, m.start()) + 1
                    secrets.append({'kind': label, 'path': f, 'line': line})
                    if len(secrets) >= 50: break
    return per_file, per_signal, secrets

def collect_tests(files: list[str]) -> dict:
    src = [f for f in files if SOURCE_FILE.search(f) and not GENERATED.search(f)]
    unit = [f for f in src if TEST_FILE.search(f) and not E2E_FILE.search(f)]
    e2e = [f for f in src if E2E_FILE.search(f)]
    stories = [f for f in files if STORY_FILE.search(f) and not f.endswith('.mdx')]
    return {'source_files': len(src), 'unit_or_component_test_files': len(unit), 'e2e_test_files': len(e2e), 'story_files': len(stories),
            'test_ratio': round(len(unit) / len(src), 2) if src else None, 'examples': {'unit': unit[:5], 'e2e': e2e[:5], 'stories': stories[:5]}}

CONVENTIONAL = re.compile(r'^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([^)]+\))?!?:\s')
PR_MERGE = re.compile(r'^Merge (pull request|branch|remote-tracking branch)|See merge request|\(#\d+\)\s*$')

def collect_git(repo: Path, since: str | None, until: str | None, author_query: str | None, max_commits: int) -> dict:
    rng = []
    if since: rng.append(f'--since={since}')
    if until: rng.append(f'--until={until}')
    fmt = '%H%x1f%an%x1f%ae%x1f%as%x1f%P%x1f%s'
    raw = git(repo, 'log', 'HEAD', f'--format={fmt}', *rng)
    commits = []
    for line in raw.splitlines():
        parts = line.split('\x1f')
        if len(parts) != 6: continue
        h, an, ae, d, parents, subject = parts
        commits.append({'hash': h, 'author': an, 'email': ae, 'date': d, 'merge': len(parents.split()) > 1, 'subject': subject})
    current_branch = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    head_commit = git(repo, 'rev-parse', '--short', 'HEAD').strip()
    origin_head = git(repo, 'symbolic-ref', '--quiet', '--short', 'refs/remotes/origin/HEAD').strip()
    default_branch = origin_head.split('/', 1)[1] if origin_head.startswith('origin/') else next((b for b in ('main', 'master', 'develop') if git(repo, 'rev-parse', '--verify', '--quiet', b).strip()), current_branch)
    tags = [t for t in git(repo, 'tag', '--list').splitlines() if t]
    remote_branches = [b for b in git(repo, 'branch', '-r').splitlines() if b.strip() and '->' not in b]
    authors: dict[str, dict] = {}
    for c in commits:
        a = authors.setdefault(c['author'], {'name': c['author'], 'commits': 0, 'merges': 0, 'first': c['date'], 'last': c['date'], 'emails': set()})
        a['commits'] += 1; a['merges'] += c['merge']; a['first'] = min(a['first'], c['date']); a['last'] = max(a['last'], c['date']); a['emails'].add(c['email'])
    non_merge = [c for c in commits if not c['merge']]
    months = Counter(c['date'][:7] for c in non_merge)
    conventional = sum(bool(CONVENTIONAL.match(c['subject'])) for c in non_merge)
    merges = [c for c in commits if c['merge']]
    pr_like = sum(bool(PR_MERGE.search(c['subject'])) for c in commits)
    reverts = [c for c in non_merge if c['subject'].startswith('Revert')]
    coauthored = int(git(repo, 'log', 'HEAD', '--format=%b', *rng).count('Co-authored-by:'))
    # numstat for commit sizes and per-author files (bounded)
    raw = git(repo, 'log', 'HEAD', '--no-merges', f'-n{max_commits}', '--format=%x1e%H%x1f%an%x1f%as%x1f%s', '--numstat', *rng)
    sizes_files, sizes_lines = [], []
    per_commit_files: dict[str, list[str]] = {}
    meta: dict[str, dict] = {}
    for block in raw.split('\x1e'):
        if not block.strip(): continue
        head, _, body = block.partition('\n')
        parts = head.split('\x1f')
        if len(parts) != 4: continue
        h, an, d, subject = parts
        fl, lines = [], 0
        for row in body.splitlines():
            cols = row.split('\t')
            if len(cols) != 3: continue
            add, dele, path = cols
            if GENERATED.search(path): continue
            fl.append(path)
            if add.isdigit(): lines += int(add)
            if dele.isdigit(): lines += int(dele)
        per_commit_files[h] = fl; meta[h] = {'author': an, 'date': d, 'subject': subject}
        sizes_files.append(len(fl)); sizes_lines.append(lines)
    def med(xs): return statistics.median(xs) if xs else None
    selected = None
    if author_query:
        q = author_query.lower()
        cands = [a for a in authors.values() if q in a['name'].lower() or any(q in e.lower() for e in a['emails'])]
        if cands: selected = max(cands, key=lambda a: a['commits'])['name']
    ranked = sorted(authors.values(), key=lambda a: -a['commits'])
    top = [{'name': a['name'], 'commits': a['commits'], 'merges': a['merges'], 'first': a['first'], 'last': a['last'], 'share': round(a['commits'] / len(commits), 2) if commits else 0} for a in ranked[:15]]
    return {
        'default_branch': default_branch, 'current_branch': current_branch, 'head_commit': head_commit, 'commits': len(commits), 'non_merge_commits': len(non_merge), 'merge_commits': len(merges), 'pr_like_merges': pr_like,
        'first_date': min((c['date'] for c in commits), default=None), 'last_date': max((c['date'] for c in commits), default=None),
        'authors': len(authors), 'top_authors': top, 'top_author_share': top[0]['share'] if top else None,
        'commits_per_month': dict(sorted(months.items())), 'conventional_commit_ratio': round(conventional / len(non_merge), 2) if non_merge else None,
        'reverts': len(reverts), 'co_authored_by': coauthored, 'tags': len(tags), 'recent_tags': tags[-5:], 'remote_branches': len(remote_branches),
        'median_files_per_commit': med(sizes_files), 'median_lines_per_commit': med(sizes_lines), 'sampled_commits_for_sizes': len(sizes_files),
        '_per_commit_files': per_commit_files, '_meta': meta, '_selected_author': selected, '_author_query': author_query,
    }

def collect_author(repo: Path, g: dict, files_set: set[str], per_file_signals: dict, bulk_threshold: int) -> dict | None:
    name = g['_selected_author']
    if not name: return None
    all_commits = [h for h, m in g['_meta'].items() if m['author'] == name]
    # A commit touching many files (initial import, mass migration, reformat) says little about any single skill: keep it apart.
    bulk = [h for h in all_commits if len(g['_per_commit_files'].get(h, [])) >= bulk_threshold]
    commits = [h for h in all_commits if h not in bulk]
    touched: Counter = Counter()
    bulk_touched: set[str] = set(p for h in bulk for p in g['_per_commit_files'].get(h, []))
    by_skill: dict[str, dict] = defaultdict(lambda: {'files': set(), 'commits': []})
    for h in commits:
        fl = g['_per_commit_files'].get(h, [])
        skills_here: set[str] = set()
        for p in fl:
            touched[p] += 1
            for s in skills_for_path(p): skills_here.add(s); by_skill[s]['files'].add(p)
        for s in skills_here:
            if len(by_skill[s]['commits']) < 6: by_skill[s]['commits'].append({'hash': h[:7], 'date': g['_meta'][h]['date'], 'subject': g['_meta'][h]['subject'][:90], 'files': len(fl)})
    # content signals of the author's touched files that still exist
    sig_by_skill: dict[str, Counter] = defaultdict(Counter)
    for p in touched:
        if p in files_set and p in per_file_signals:
            for k, n in per_file_signals[p].items():
                for s in SIGNALS[k][1]: sig_by_skill[s][k] += n
    skills = {}
    for s, d in by_skill.items():
        skills[s] = {'files_touched': len(d['files']), 'sample_files': sorted(d['files'])[:6], 'sample_commits': d['commits'], 'content_signals': {k: {'hits': n, 'label': SIGNALS[k][2]} for k, n in sig_by_skill.get(s, Counter()).most_common(6)}}
    author_merges = next((a['merges'] for a in g['top_authors'] if a['name'] == name), 0)
    subjects = [g['_meta'][h]['subject'] for h in commits]
    deleted = sum(1 for p in touched if p not in files_set)
    notes = []
    if bulk: notes.append(f"一括コミット {len(bulk)} 件（{bulk_threshold} ファイル以上）を要素技術ごとの集計から除外：" + '、'.join(f"{h[:7]}（{len(g['_per_commit_files'].get(h, []))} ファイル、{g['_meta'][h]['date']}）" for h in bulk[:5]))
    if author_merges and len(all_commits) <= max(2, author_merges // 5): notes.append(f"非マージ {len(all_commits)} 件に対しマージ {author_merges} 件：取り込み・レビュー役の可能性が高い。git.collaboration 以外の根拠には数えない")
    if deleted: notes.append(f"触れたファイルのうち {deleted} 件は現在のツリーに存在しない（削除・移動済み。内容の手がかりは現存ファイルのみ）")
    tests_touched = sum(1 for p in touched if TEST_FILE.search(p) or E2E_FILE.search(p))
    docs_touched = sum(1 for p in touched if p.endswith(('.md', '.mdx')))
    ci_touched = sum(1 for p in touched if re.search(r'(^|/)\.github/|\.gitlab-ci', p))
    return {'name': name, 'commits': len(all_commits), 'commits_excluding_bulk': len(commits), 'bulk_commits': [{'hash': h[:7], 'date': g['_meta'][h]['date'], 'files': len(g['_per_commit_files'].get(h, [])), 'subject': g['_meta'][h]['subject'][:90]} for h in bulk], 'bulk_files_touched': len(bulk_touched), 'files_no_longer_present': deleted, 'notes': notes, 'merges_by_author': author_merges, 'files_touched': len(touched), 'test_files_touched': tests_touched, 'doc_files_touched': docs_touched, 'ci_files_touched': ci_touched,
            'conventional_commit_ratio': round(sum(bool(CONVENTIONAL.match(s)) for s in subjects) / len(subjects), 2) if subjects else None,
            'most_touched_files': [{'path': p, 'commits': n} for p, n in touched.most_common(12)], 'skills': dict(sorted(skills.items(), key=lambda kv: -kv[1]['files_touched']))}

def team_facts(stack, configs, ci, tests, per_signal, secrets, g, strict) -> dict:
    ci_checks = Counter(k for w in ci for k in w['checks'])
    def has(label): return label in configs
    def sig(k): return per_signal[k]['files']
    f: dict[str, list[str]] = defaultdict(list)
    f['1-1'] += [f"型付け言語：{'TypeScript' if 'TypeScript' in ' '.join(stack['tools']) else '未検出'}（tsconfig strict: {strict}）", f"ESLint: {has('ESLint') or has('Biome')}、Prettier: {has('Prettier') or has('Biome')}、CI の lint: {ci_checks['lint']} 件、typecheck: {ci_checks['typecheck']} 件",
                 f"any／@ts-ignore を含むファイル {sig('ts_escape')}、eslint-disable {sig('lint_disable')}、console.log {sig('console_log')}、TODO/FIXME {sig('todo')}", f"コミットの中央値：{g['median_files_per_commit']} ファイル／{g['median_lines_per_commit']} 行、規約準拠率 {g['conventional_commit_ratio']}"]
    f['1-2'] += [f"Node 指定: {stack['node']}、パッケージマネージャ: {stack['package_manager']}、.env.example: {has('.env.example')}、Dev Container: {has('Dev Container')}、Docker: {has('Dockerfile') or has('docker-compose')}", f"README: {has('README')}、CONTRIBUTING: {has('CONTRIBUTING')}、scripts: {', '.join(list(stack['scripts'])[:12])}"]
    f['1-3'] += [f"UI フレームワーク: {', '.join(t for t in stack['tools'] if t.split()[0] in ('React', 'Next.js', 'Vue', 'Nuxt', 'Svelte', 'Angular', 'Astro', 'Solid')) or '未検出'}", f"Storybook: {has('Storybook')}（ストーリー {tests['story_files']} 件）、cva／shadcn: {sig('cva_shadcn')} ファイル、CSS 変数: {sig('css_vars')} ファイル"]
    f['1-4'] += [f"状態管理: {', '.join(t for t in stack['tools'] if t in ('Zustand', 'Redux Toolkit', 'Jotai', 'Valtio', 'TanStack Query', 'SWR')) or '未検出'}、Context/useReducer {sig('context_reducer')} ファイル", f"ADR／設計記録: {has('ADR／設計記録')}、docs: {has('docs ディレクトリ')}、OpenAPI 定義: {has('OpenAPI 定義')}"]
    f['1-5'] += [f"依存パッケージ数 {stack.get('dependency_count')}、ADR: {has('ADR／設計記録')}、CHANGELOG: {has('CHANGELOG')}"]
    f['2-1'] += [f"CI の性能検査 {ci_checks['performance']} 件、Lighthouse CI config: {has('Lighthouse CI config')}、web-vitals {sig('web_vitals')} ファイル、next/image・font {sig('next_image')}、動的インポート {sig('dynamic_import')}、キャッシュ制御 {sig('cache_control')}"]
    f['2-2'] += [f"CI の a11y 検査 {ci_checks['accessibility']} 件、axe {sig('axe')} ファイル、jsx-a11y: {'eslint-plugin-jsx-a11y' in stack['tools']}、ARIA/role {sig('aria')} ファイル、alt/lang {sig('alt_lang')}、セマンティック要素 {sig('semantic')}"]
    f['2-3'] += [f"SAST {ci_checks['SAST']} 件、依存監査 {ci_checks['dependency audit']} 件、秘密情報スキャン {ci_checks['secret scan']} 件、Renovate/Dependabot: {has('Renovate／Dependabot')}、SECURITY.md: {has('SECURITY.md')}", f"セキュリティヘッダー {sig('csp')} ファイル、サニタイズ {sig('sanitize')}、危険な出力・eval {sig('dangerous')}、認証 {sig('auth')}", f"機密情報らしき文字列の検出：{len(secrets)} 件" + (f"（例：{secrets[0]['path']}:{secrets[0]['line']} {secrets[0]['kind']}）" if secrets else '')]
    f['2-4'] += [f"解析ツール {sig('analytics')} ファイル、Cookie の扱い {sig('cookies')}、locales: {has('locales（多言語）')}"]
    f['2-5'] += [f"デザイントークン／CSS 変数 {sig('css_vars')} ファイル、Tailwind: {has('Tailwind config') or 'Tailwind CSS' in ' '.join(stack['tools'])}、Style Dictionary: {'Style Dictionary' in stack['tools']}、Storybook: {has('Storybook')}"]
    f['3-1'] += [f"テストファイル {tests['unit_or_component_test_files']}（ソース {tests['source_files']}、比率 {tests['test_ratio']}）、E2E {tests['e2e_test_files']}、Testing Library {sig('testing_library')} ファイル、MSW {sig('msw')}", f"CI の unit tests {ci_checks['unit tests']} 件、e2e {ci_checks['e2e']} 件、sharding/matrix {ci_checks['sharding']} 件、codecov: {has('codecov config')}"]
    f['3-2'] += [f"CI の build {ci_checks['build']} 件、cache {ci_checks['cache']} 件、lockfile: {stack['package_manager']}、Vite/Next config: {has('Vite config') or has('Next.js config')}"]
    f['3-3'] += [f"CI の deploy {ci_checks['deploy']} 件、environments {ci_checks['environments']} 件、デプロイ設定: {has('Vercel／Netlify config') or has('Dockerfile') or has('Kubernetes manifests')}、タグ {g['tags']} 件（直近 {', '.join(g['recent_tags'])}）、revert {g['reverts']} 件"]
    f['3-4'] += [f"Renovate/Dependabot: {has('Renovate／Dependabot')}、依存監査 {ci_checks['dependency audit']} 件、lockfile: {stack['package_manager']}"]
    f['3-5'] += [f"CI 定義 {len(ci)} 件、pull_request トリガー {ci_checks['pull_request trigger']} 件、concurrency {ci_checks['concurrency']} 件、continue-on-error {ci_checks['continue-on-error']} 件、PR らしきマージ {g['pr_like_merges']} 件／マージ {g['merge_commits']} 件"]
    f['4-1'] += [f"'use server' {sig('use_server')} ファイル、API 層 (fetch {sig('fetch')}、axios {sig('axios')}、TanStack/SWR {sig('query')})、OpenAPI 生成 {sig('openapi')}、認証 {sig('auth')}"]
    f['4-2'] += [f"IaC: {has('IaC（Terraform／CDK）')}、Kubernetes: {has('Kubernetes manifests')}、Docker: {has('Dockerfile')}、.env.example: {has('.env.example')}"]
    f['4-3'] += [f"HTTP キャッシュ制御 {sig('cache_control')} ファイル、再検証 {sig('revalidate')}、サーバー状態キャッシュ {sig('query')}"]
    f['4-4'] += [f"監視・エラー収集 {sig('monitoring')} ファイル、Sentry config: {has('Sentry config')}、web-vitals {sig('web_vitals')}"]
    f['4-5'] += [f"RUNBOOK／インシデント手順らしきファイル（要確認）: {has('RUNBOOK／インシデント手順らしきファイル（要確認）')}、revert {g['reverts']} 件、タグ {g['tags']} 件"]
    f['5-1'] += [f"docs: {has('docs ディレクトリ')}、ADR: {has('ADR／設計記録')}、Co-authored-by {g['co_authored_by']} 件、作者数 {g['authors']}、最多作者の比率 {g['top_author_share']}"]
    f['5-2'] += [f"共通部品の兆候：components/ {sig('cva_shadcn')} ファイル、Storybook: {has('Storybook')}、workspaces: {stack['workspaces'] or stack['pnpm_workspace']}"]
    f['5-3'] += [f"CODEOWNERS: {has('CODEOWNERS')}、CONTRIBUTING: {has('CONTRIBUTING')}、PR テンプレート: {has('PR template')}、Issue テンプレート: {has('Issue templates')}"]
    f['5-4'] += [f"Issue/PR テンプレート: {has('PR template') or has('Issue templates')}、フィーチャーフラグ {sig('feature_flags')} ファイル、解析ツール {sig('analytics')}"]
    f['5-5'] += [f"README: {has('README')}、LICENSE: {has('LICENSE')}、CHANGELOG: {has('CHANGELOG')}"]
    return dict(f)

def sub_titles() -> dict[str, str]:
    """Sub-theme names from the bundled checklist catalog (optional: the script also works without it)."""
    items = load_json(Path(__file__).resolve().parent.parent / 'references' / 'checklist-items.json')
    return {i['sub']: i['subtitle'] for i in items} if isinstance(items, list) else {}

def write_markdown(ev: dict, out: Path):
    L = []
    g = ev['git']; st = ev['stack']
    L += [f"# 根拠の要約：{ev['repo']['name']}", '', f"- パス：`{ev['repo']['path']}`（既定ブランチ `{g['default_branch']}`、現在のブランチ `{g['current_branch']}`、評価時点のコミット `{g['head_commit']}`）", f"- 期間：{ev['repo']['since'] or '全期間'} 〜 {ev['repo']['until'] or ev['repo']['generated']}（コミット {g['commits']} 件、うちマージ {g['merge_commits']} 件、作者 {g['authors']} 人、{g['first_date']} 〜 {g['last_date']}）", f"- 追跡ファイル：{ev['repo']['tracked_files']} 件（内容を走査したファイル {ev['repo']['scanned_files']} 件）", '']
    L += ['## 技術スタック', '', f"- 検出したツール：{', '.join(st['tools']) or 'なし'}", f"- パッケージマネージャ：{st['package_manager']}、Node：{st['node']}、依存パッケージ数：{st.get('dependency_count')}、workspaces：{st['workspaces'] or st['pnpm_workspace']}", f"- scripts：{', '.join(f'`{k}`' for k in list(st['scripts'])[:16]) or 'なし'}", '']
    L += ['## 設定・文書', '', '| 項目 | ファイル |', '| :--- | :--- |'] + [f"| {k} | {', '.join(f'`{p}`' for p in v)} |" for k, v in ev['configs'].items()] + [f"| tsconfig strict | {ev['tsconfig_strict']} |", '']
    L += ['## CI/CD', '']
    L += ([f"- `{w['path']}`（{w['name'] or '無題'}）：{', '.join(w['checks']) or '検査なし'}" for w in ev['ci']] or ['- CI 定義なし']) + ['']
    t = ev['tests']
    L += ['## テスト', '', f"- ソース {t['source_files']} ファイル、ユニット／コンポーネントテスト {t['unit_or_component_test_files']}（比率 {t['test_ratio']}）、E2E {t['e2e_test_files']}、ストーリー {t['story_files']}", f"- 例：{', '.join(f'`{p}`' for p in (t['examples']['unit'][:3] + t['examples']['e2e'][:2]))}", '']
    L += ['## ソースの手がかり（リポジトリ全体）', '', '| 手がかり | ファイル数 | 一致数 | 例 |', '| :--- | ---: | ---: | :--- |']
    for k, v in sorted(ev['signals'].items(), key=lambda kv: -kv[1]['files']):
        if v['files']: L.append(f"| {SIGNALS[k][2]} | {v['files']} | {v['hits']} | {', '.join(f'`{p}`' for p in v['examples'])} |")
    L += ['', '## 機密情報らしき文字列', '']
    L += ([f"- {s['kind']}：`{s['path']}:{s['line']}`" for s in ev['secrets']] or ['- 検出なし（.env.example、テスト、ドキュメント、lockfile は対象外）']) + ['']
    L += ['## Git 履歴', '', f"- Conventional Commits 形式の件名の比率 {g['conventional_commit_ratio']}（別の規約を使うチームでは低くて当然。件名の一貫性は作者別の一覧で確認）、PR らしきマージ {g['pr_like_merges']} 件、revert {g['reverts']} 件、Co-authored-by {g['co_authored_by']} 件、タグ {g['tags']} 件、リモートブランチ {g['remote_branches']} 件", f"- 1コミットの中央値：{g['median_files_per_commit']} ファイル、{g['median_lines_per_commit']} 行（標本 {g['sampled_commits_for_sizes']} 件）", f"- 月別コミット数：{', '.join(f'{m} {n}' for m, n in list(g['commits_per_month'].items())[-12:])}", '', '| 作者 | コミット | マージ | 期間 | 比率 |', '| :--- | ---: | ---: | :--- | ---: |']
    L += [f"| {a['name']} | {a['commits']} | {a['merges']} | {a['first']} 〜 {a['last']} | {a['share']} |" for a in g['top_authors']] + ['']
    au = ev['author']
    L += ['## 対象者の活動', '']
    if not au:
        L += [f"- 対象者が指定されていないか一致しませんでした（指定：{g.get('author_query')}）。上の作者一覧から選んでください。", '']
    else:
        L += [f"- {au['name']}：非マージコミット {au['commits']} 件（うち一括 {len(au['bulk_commits'])} 件を除いた {au['commits_excluding_bulk']} 件を集計）、マージ {au['merges_by_author']} 件、触れたファイル {au['files_touched']}（テスト {au['test_files_touched']}、文書 {au['doc_files_touched']}、CI {au['ci_files_touched']}）、Conventional Commits 比率 {au['conventional_commit_ratio']}"] + [f"- 注意：{n}" for n in au['notes']] + [f"- よく触れたファイル：{', '.join('`' + x['path'] + '`(' + str(x['commits']) + ')' for x in au['most_touched_files'][:8])}", '', '### 要素技術ごとの手がかり', '']
        for s, d in au['skills'].items():
            sig = '、'.join(f"{v['label']} {v['hits']}" for v in d['content_signals'].values())
            L += [f"- **`{s}`**：触れたファイル {d['files_touched']}" + (f"。内容：{sig}" if sig else ''), f"  - 例：{', '.join(f'`{p}`' for p in d['sample_files'][:4])}"] + [f"  - `{c['hash']}` {c['date']} {c['subject']}（{c['files']} ファイル）" for c in d['sample_commits'][:4]]
        L.append('')
    titles = sub_titles()
    L += ['## チームチェックの小テーマごとの事実', '']
    for sub, facts in ev['team'].items(): L += [f"### {sub} {titles.get(sub, '')}".rstrip(), ''] + [f"- {x}" for x in facts] + ['']
    (out / 'evidence.md').write_text('\n'.join(L), encoding='utf-8')

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('repo'); ap.add_argument('--author'); ap.add_argument('--since'); ap.add_argument('--until'); ap.add_argument('--out'); ap.add_argument('--max-files', type=int, default=4000); ap.add_argument('--max-commits', type=int, default=3000); ap.add_argument('--bulk-threshold', type=int, default=30, help='この数以上のファイルに触れたコミットは一括コミットとして要素技術の集計から除外')
    a = ap.parse_args()
    repo = Path(a.repo).expanduser().resolve()
    top = git(repo, 'rev-parse', '--show-toplevel').strip()
    if not top: sys.exit(f'{repo} は git リポジトリではありません。')
    repo = Path(top)
    out = Path(a.out).expanduser().resolve() if a.out else Path.cwd() / 'assessment-draft' / repo.name
    if out.is_relative_to(repo) if hasattr(out, 'is_relative_to') else str(out).startswith(str(repo)):
        print(f'注意：出力先 {out} は対象リポジトリの中です。コミットしないよう .gitignore を確認してください。', file=sys.stderr)
    out.mkdir(parents=True, exist_ok=True)
    files = tracked_files(repo)
    scan_files = files[:a.max_files]
    stack = collect_stack(repo, files); configs = collect_configs(files); ci = collect_ci(repo, files); tests = collect_tests(files); strict = tsconfig_strict(repo, files)
    per_file, per_signal, secrets = scan_contents(repo, scan_files)
    g = collect_git(repo, a.since, a.until, a.author, a.max_commits)
    author = collect_author(repo, g, set(files), per_file, a.bulk_threshold)
    team = team_facts(stack, configs, ci, tests, per_signal, secrets, g, strict)
    public_git = {k: v for k, v in g.items() if not k.startswith('_')}; public_git['author_query'] = a.author
    ev = {'generator': 'assessment-draft/collect_evidence.py', 'repo': {'name': repo.name, 'path': str(repo), 'since': a.since, 'until': a.until, 'generated': date.today().isoformat(), 'tracked_files': len(files), 'scanned_files': len(scan_files)},
          'stack': stack, 'configs': configs, 'tsconfig_strict': strict, 'ci': ci, 'tests': tests, 'signals': per_signal, 'secrets': secrets, 'git': public_git, 'author': author, 'team': team,
          'signal_labels': {k: {'label': v[2], 'skills': v[1]} for k, v in SIGNALS.items()}}
    (out / 'evidence.json').write_text(json.dumps(ev, ensure_ascii=False, indent=1), encoding='utf-8')
    write_markdown(ev, out)
    print(f'evidence written: {out / "evidence.md"} ({len(files)} files, {g["commits"]} commits' + (f', author: {author["name"]}' if author else ', author: none') + ')')

if __name__ == '__main__':
    main()
