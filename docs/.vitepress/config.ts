import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import container from 'markdown-it-container'
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
const root = new URL('../../', import.meta.url)
const catalog = JSON.parse(readFileSync(new URL('build/document-map.json', root), 'utf8'))
const { version } = JSON.parse(readFileSync(new URL('package.json', root), 'utf8'))
const pages = catalog.pages
const repository = process.env.GITHUB_REPOSITORY || ''
const [owner, repo] = repository.split('/')
const defaultBase = repo ? (repo.toLowerCase() === `${owner}.github.io`.toLowerCase() ? '/' : `/${repo}/`) : '/frontend-engineering-guide/'
const requestedBase = process.env.SITE_BASE_PATH ?? defaultBase
const base = '/' + requestedBase.replace(/^\/+|\/+$/g, '') + (requestedBase.replace(/\//g, '') ? '/' : '')
const origin = (process.env.SITE_ORIGIN || '').replace(/\/$/, '')
const url = (p: { path: string }) => '/' + p.path.replace(/index\.md$/, '').replace(/\.md$/, '')
const item = (p: any) => ({ text: p.title, link: url(p) })
const by = (kind: string) => pages.filter((p: any) => p.kind === kind)
const guide = [{ text: '使い方ガイド', items: by('guide').map(item) }]
const skills = [
  { text: '要素技術', link: '/skills/', items: [] },
  { text: '習熟度マトリクス', link: '/skills/matrix', items: [] },
  ...catalog.areas.map((a: any) => ({ text: a.title, link: `/skills/${a.id}/`, collapsed: true, items: by('skill').filter((p: any) => p.area === a.id).map(item) }))
]
const checks = [
  { text: 'チームチェック', link: '/checklists/', items: [] },
  ...[...new Set(by('checklist').map((p: any) => p.section as string))].map(section => ({ text: section, collapsed: true, items: by('checklist').filter((p: any) => p.section === section).map((p: any) => ({ text: `${p.sourceId} ${p.title}`, link: url(p) })) }))
]
const forms = [{ text: '記録書式', link: '/templates/', items: by('template').map(item) }, { text: '記入例', link: '/examples/', items: by('example').map(item) }, { text: 'ダウンロード', link: '/downloads', items: [] }]
const maintenance = [{ text: '運用・改訂', items: by('maintenance').map(item) }]
const ordered = pages.filter((p: any) => p.handbook)
export default withMermaid(defineConfig({
  lang: 'ja-JP', title: 'フロントエンド習熟度ガイド', titleTemplate: ':title | 習熟度ガイド',
  description: '31の要素技術の習熟度と100項目のチームチェック。共通の基準で評価し、育成と開発環境の改善につなげます。',
  base, cleanUrls: false, appearance: true,
  srcExclude: ['public/**'],
  // Mermaid: keep Japanese node labels on one line instead of wrapping at the 200px default.
  mermaid: { flowchart: { wrappingWidth: 360 } },
  head: [['link', { rel: 'icon', type: 'image/svg+xml', href: `${base}assets/favicon.svg` }]],
  ...(origin ? { sitemap: { hostname: origin + base } } : {}),
  markdown: {
    lineNumbers: false,
    config(md) {
      // ::: example … ::: marks this guide's sample answers apart from the source text.
      md.use(container, 'example', {
        render: (tokens: any[], idx: number) => tokens[idx].nesting === 1
          ? '<div class="answer-example"><p class="answer-example-title">望ましい回答例<span>架空の記入例。実際の回答には実態と根拠を記載</span></p>\n'
          : '</div>\n'
      })
      // ::: start … ::: is the first step toward Lv1 on each element-technology page.
      md.use(container, 'start', {
        render: (tokens: any[], idx: number) => tokens[idx].nesting === 1
          ? '<div class="first-step"><p class="first-step-title">はじめの一歩<span>Lv1へ向けて最初に学ぶこと</span></p>\n'
          : '</div>\n'
      })
    }
  },
  vite: { server: { fs: { allow: [fileURLToPath(root)] } } },
  transformPageData(pageData) {
    const i = ordered.findIndex((p: any) => p.path === pageData.relativePath)
    if (i >= 0) {
      pageData.frontmatter.prev = i > 0 ? item(ordered[i - 1]) : false
      pageData.frontmatter.next = i < ordered.length - 1 ? item(ordered[i + 1]) : false
    }
  },
  themeConfig: {
    siteTitle: 'フロントエンド習熟度ガイド',
    nav: [
      { text: '使い方', link: '/guide/overview', activeMatch: '/guide/' },
      { text: '要素技術', link: '/skills/', activeMatch: '/skills/' },
      { text: 'チームチェック', link: '/checklists/', activeMatch: '/checklists/' },
      { text: '書式・記入例', link: '/templates/', activeMatch: '/(templates|examples)/' },
      { text: '運用・改訂', link: '/maintenance/', activeMatch: '/maintenance/' },
      { text: 'ダウンロード', link: '/downloads' }
    ],
    sidebar: {
      '/guide/': guide, '/skills/': skills, '/checklists/': checks,
      '/templates/': forms, '/examples/': forms, '/maintenance/': maintenance,
      '/downloads': forms
    },
    ...(repository ? { socialLinks: [{ icon: 'github', link: `https://github.com/${repository}` }], editLink: { pattern: `https://github.com/${repository}/edit/main/docs/:path`, text: 'GitHubで編集を提案' } } : {}),
    outline: { level: [2, 3], label: 'このページの内容' },
    docFooter: { prev: '前のページ', next: '次のページ' },
    sidebarMenuLabel: '目次', returnToTopLabel: 'ページの先頭へ',
    darkModeSwitchLabel: '表示モード', lightModeSwitchTitle: 'ライトモード', darkModeSwitchTitle: 'ダークモード',
    skipToContentLabel: '本文へ移動',
    footer: { message: 'チェック項目の原文：一般社団法人日本CTO協会「<a href="https://dxcriteria.cto-a.org/frontend" target="_blank" rel="noopener">Webフロントエンド版DX Criteria</a>」（<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ja" target="_blank" rel="noopener">CC BY-SA 4.0</a>）', copyright: `本ガイド全体：<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ja" target="_blank" rel="noopener">CC BY-SA 4.0</a> · 公開基準・空の書式・架空の回答例 · 文書版 ${version}` },
    search: {
      provider: 'local',
      options: {
        locales: { root: { translations: {
          button: { buttonText: '検索', buttonAriaLabel: '文書を検索' },
          modal: { displayDetails: '詳細を表示', resetButtonTitle: '検索をクリア', backButtonTitle: '検索を閉じる', noResultsText: '結果が見つかりません', footer: { selectText: '選択', selectKeyAriaLabel: 'Enter', navigateText: '移動', navigateUpKeyAriaLabel: '上矢印', navigateDownKeyAriaLabel: '下矢印', closeText: '閉じる', closeKeyAriaLabel: 'Escape' } }
        } } },
        miniSearch: {
          options: {
            // VitePress serializes this function for the browser: keep it self-contained.
            tokenize: (text: string) => {
              const input = text.normalize('NFKC').toLowerCase()
              const terms = new Set<string>()
              // Deterministic tokens avoid ICU differences between Node and browsers.
              for (const match of input.matchAll(/[a-z0-9]+(?:[.\-][a-z0-9]+)*/g)) {
                terms.add(match[0])
                for (const part of match[0].split(/[.\-]/)) terms.add(part)
              }
              for (const match of input.matchAll(/[\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}ー]+/gu)) {
                const chars = Array.from(match[0])
                for (let i = 0; i < chars.length; i++) {
                  terms.add(chars[i])
                  if (i + 1 < chars.length) terms.add(chars[i] + chars[i + 1])
                }
              }
              return [...terms]
            },
            processTerm: (term: string) => term.toLowerCase()
          },
          searchOptions: { prefix: true, fuzzy: false, combineWith: 'AND' }
        }
      }
    }
  }
}))
