import assert from 'node:assert/strict';
import { chromium, expect } from '@playwright/test';
import { createServer } from 'node:http';
import { readFile, stat, mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
const validation = spawnSync('python3', ['scripts/check_html.py'], { stdio: 'inherit' });
if (validation.status !== 0) process.exit(validation.status ?? 1);
const directory = path.resolve('docs/.vitepress/dist');
const homeHtml = await readFile(path.join(directory, 'index.html'), 'utf8');
const base = homeHtml.match(/href="([^"]*)assets\/favicon.svg"/)[1];
const mime = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.md': 'text/markdown; charset=utf-8', '.zip': 'application/zip', '.woff2': 'font/woff2' };
const server = createServer(async (req, res) => {
  try {
    let pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (!pathname.startsWith(base)) { res.writeHead(404); res.end(); return; }
    let file = path.resolve(directory, pathname.slice(base.length) || 'index.html');
    if (!file.startsWith(directory + path.sep)) { res.writeHead(404); res.end(); return; }
    if (pathname.endsWith('/')) file = path.join(file === path.join(directory, 'index.html') ? directory : file, 'index.html');
    const info = await stat(file);
    if (!info.isFile()) throw Error('Not a file');
    res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream' }); res.end(await readFile(file));
  } catch { res.writeHead(404); res.end('Not found'); }
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const origin = `http://127.0.0.1:${server.address().port}`;
const url = origin + base;
const results = { base, pages: 84, definitions: 155, checklistItems: 100, checks: [] };
let browser;
try {
  browser = await chromium.launch({ headless: true, ...(process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH, args: JSON.parse(process.env.PLAYWRIGHT_CHROMIUM_ARGS || '["--no-sandbox","--disable-dev-shm-usage"]') } : {}) });
  results.browser = browser.version();
  const page = await browser.newPage({ viewport: { width: 1440, height: 1050 } });
  const errors = []; const networkErrors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('response', response => { if (response.url().startsWith(origin) && response.status() >= 400) networkErrors.push(response.url()); });
  await page.goto(url);
  await expect(page.locator('h1')).toHaveText('フロントエンド習熟度ガイド');
  await expect(page.getByRole('link', { name: '要素技術', exact: true }).first()).toBeVisible();
  await mkdir('artifacts', { recursive: true });
  await page.screenshot({ path: 'artifacts/home-desktop.png', fullPage: true });
  results.checks.push('desktop home and navigation');

  for (const [route, heading, anchor] of [['skills/implementation/react.form.html#lv3', 'フォーム実装', 'lv3'], ['checklists/security.html#_2-3-1-メトリクスの計測', 'セキュリティ', '_2-3-1-メトリクスの計測'], ['guide/glossary.html#カスケードと詳細度', '用語集', 'カスケードと詳細度']]) {
    await page.goto(url + route); await page.reload();
    await expect(page.locator('h1')).toHaveText(heading);
    await expect(page.locator(`[id="${anchor.normalize("NFKD")}"]`)).toBeVisible(); // VitePress keeps heading ids in NFKD
  }
  results.checks.push('deep links, anchor navigation and refresh');

  await page.goto(url + 'guide/prerequisites.html');
  await expect(page.locator('.mermaid svg')).toHaveCount(2, { timeout: 15000 });
  await expect(page.locator('.mermaid svg').nth(1)).toBeVisible();
  results.checks.push('mermaid sequence and flow diagrams render');

  await page.goto(url + 'skills/matrix.html');
  await expect(page.locator('h1')).toHaveText('習熟度マトリクス');
  await expect(page.locator('.skill-matrix')).toHaveCount(4); // one table per area
  await expect(page.locator('.skill-matrix tbody tr')).toHaveCount(31);
  await expect(page.locator('.skill-matrix tbody tr:has(a[href*="web.basic"]) td')).toHaveCount(6);
  await expect(page.locator('.skill-matrix tbody tr:has(a[href*="web.basic"]) td').nth(5)).not.toBeEmpty();
  results.checks.push('skill matrix: four area tables, 31 rows by five levels');

  const lv2 = page.locator('.skill-matrix tbody tr:has(a[href*="web.basic"]) td.lv-cell').nth(2);
  await expect(lv2).toHaveAttribute('aria-pressed', 'false');
  await lv2.click();
  await expect(lv2).toHaveAttribute('aria-pressed', 'true');
  await expect(page.locator('.matrix-stats .stat-primary strong')).toContainText('1');
  await page.reload();
  await expect(page.locator('.skill-matrix tbody tr:has(a[href*="web.basic"]) td.lv-cell').nth(2)).toHaveAttribute('aria-pressed', 'true'); // persisted in localStorage
  await expect(page.locator('.skill-matrix tbody tr:has(a[href*="web.basic"]) .row-level')).toHaveText('Lv2');
  await expect(page.locator('.matrix-markdown pre')).toContainText('- Web基礎（`web.basic`）：Lv2 画面表示やAPI呼び出しの通信を追跡し'); // level plus its definition
  const md = await page.locator('.matrix-markdown pre').textContent(); // textContent: the details element is collapsed
  const tally = md.indexOf('| 基礎領域 | 1 / 5 | 0 | 0 | 1 | 0 | 0 | 4 |'), heading = md.indexOf('## 基礎領域（評価済み 1 / 5、未評価 4）');
  assert.ok(tally >= 0 && heading > tally, 'markdown copy: per-area tally table precedes the per-skill lines');
  assert.ok(md.includes('| 合計 | 1 / 31 | 0 | 0 | 1 | 0 | 0 | 30 |'), 'markdown copy: total row');
  results.checks.push('self-assessment on the matrix persists across reloads, markdown copy carries the per-area tally');

  const sidebar = page.locator('.VPSidebar');
  const fullWidth = (await sidebar.boundingBox()).width;
  await page.getByRole('button', { name: '目次をコンパクト表示' }).click();
  await expect(page.locator('html')).toHaveAttribute('data-sidebar', 'compact');
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-sidebar', 'compact'); // persisted and applied before paint
  const compactWidth = (await sidebar.boundingBox()).width;
  if (!(compactWidth < fullWidth - 150)) throw Error(`Compact sidebar not narrower: ${compactWidth} vs ${fullWidth}`);
  await page.screenshot({ path: 'artifacts/matrix-compact.png' });
  await page.getByRole('button', { name: '目次を表示' }).click();
  await expect(page.locator('html')).toHaveAttribute('data-sidebar', 'full');
  results.checks.push('sidebar full / compact toggle persists');

  for (const [query, target] of [['react.form', 'react.form'], ['2-3-1', 'security'], ['セキュリティ', 'security'], ['非同期', 'javascript.async']]) {
    await page.locator('button.DocSearch-Button').click();
    const input = page.locator('#localsearch-input');
    await expect(input).toBeVisible(); await input.fill(query);
    const result = page.locator(`.VPLocalSearchBox a[href*="${target}"]`).first();
    try { await expect(result).toBeVisible({ timeout: 15000 }); } catch (e) { console.error('Search diagnostics', query, await page.locator('.VPLocalSearchBox').innerText(), errors, networkErrors); await page.screenshot({path: 'artifacts/search-failure.png'}); throw e; }
    await result.click();
    await expect(input).toBeHidden();
    results.checks.push(`search ${query}`);
  }
  await page.locator('button.DocSearch-Button').click();
  await page.locator('#localsearch-input').fill('存在しない検索語zzzzzzzz');
  await expect(page.getByText('結果が見つかりません')).toBeVisible();
  await page.keyboard.press('Escape');
  results.checks.push('empty search and keyboard close');

  await page.goto(url + 'downloads.html');
  await expect(page.locator('.downloads-list a')).toHaveCount(6);
  for (const anchor of await page.locator('.downloads-list a').all()) {
    const [download] = await Promise.all([page.waitForEvent('download'), anchor.click()]);
    if (await download.failure()) throw Error('Download failed');
  }
  results.checks.push('six browser downloads');

  await page.goto(url + 'checklists/security.html');
  await expect(page.locator('.team-item')).toHaveCount(4); // one widget per item, after its 望ましい回答例
  await expect(page.locator('.supplement .supplement-title').first()).toHaveText('補足'); // the source's note sits apart from the criterion
  await expect(page.locator('.answer-example li').first()).toBeVisible(); // sample answers are bulleted, one sentence each
  const item1 = page.locator('.team-item[data-sid="2-3-1"]'); const item4 = page.locator('.team-item[data-sid="2-3-4"]');
  await item1.getByRole('button', { name: 'はい', exact: true }).click();
  await expect(item1.locator('.team-score')).toHaveText('1点');
  await item1.locator('textarea').fill('PRごとにSASTを実行。例外は期限付きで記録。');
  await item4.getByRole('button', { name: 'はい', exact: true }).click();
  await expect(item4.locator('.team-score')).toHaveText('0点'); // anti-pattern: はい scores 0
  await item4.getByRole('button', { name: 'いいえ、でも…', exact: true }).click();
  await expect(item4.locator('.team-score')).toHaveText('0.5点');
  await expect(page.locator('.team-assessment .stat-primary strong')).toContainText('1.5');
  await page.reload();
  await expect(page.locator('.team-item[data-sid="2-3-1"] textarea')).toHaveValue('PRごとにSASTを実行。例外は期限付きで記録。'); // persisted
  await expect(page.locator('.team-item[data-sid="2-3-1"] .team-option.selected')).toHaveText('はい');
  await expect(page.locator('.matrix-markdown pre')).toContainText('- 2-3-1 メトリクスの計測：はい（1点）');
  await page.goto(url + 'checklists/');
  await expect(page.locator('.team-summary-table tbody tr')).toHaveCount(30); // 5 themes + 25 sub-themes
  await expect(page.locator('.team-assessment .stat-primary strong')).toContainText('1.5');
  await expect(page.locator('.team-item')).toHaveCount(100); // every item answerable on the index page
  await expect(page.locator('.team-item[data-sid="2-3-1"] .team-option.selected')).toHaveText('はい'); // shared storage with the sub-theme page
  await page.locator('.team-item[data-sid="1-1-1"]').getByRole('button', { name: 'はい', exact: true }).click();
  await expect(page.locator('.team-assessment .stat-primary strong')).toContainText('2.5');
  const teamMd = await page.locator('.matrix-markdown pre').textContent(); // textContent: the details element is collapsed
  const themeRow = teamMd.indexOf('| 2. ユーザー体験を支える品質 | 2 / 20 | 1.5 / 20 |'), themeHeading = teamMd.indexOf('## 2. ユーザー体験を支える品質（得点 1.5 / 20、回答 2 / 20）'), subHeading = teamMd.indexOf('### 2-3 セキュリティ（得点 1.5 / 4、回答 2 / 4）');
  assert.ok(themeRow >= 0 && themeHeading > themeRow && subHeading > themeHeading, 'team markdown copy: per-theme tally table, then theme and sub-theme headings with tallies');
  assert.ok(teamMd.includes('| 合計 | 3 / 100 | 2.5 / 100 |'), 'team markdown copy: total row');
  results.checks.push('team checklist answers, anti-pattern scoring, and the index page with all 100 items persist; markdown copy carries the per-theme tally');

  await page.goto(url + 'skills/quality/web.security.html');
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.screenshot({ path: 'artifacts/skill-dark.png', fullPage: true });
  results.checks.push('dark theme');

  await page.setViewportSize({ width: 390, height: 844 });
  await page.emulateMedia({ colorScheme: 'light' });
  await page.goto(url + 'checklists/security.html');
  await expect(page.locator('h1')).toHaveText('セキュリティ');
  await page.getByRole('button', { name: '目次', exact: true }).click();
  await expect(page.locator('.VPSidebar')).toBeVisible();
  await page.locator('.VPBackdrop').click({ position: { x: 370, y: 300 } });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  if (overflow) throw Error('Horizontal page overflow on mobile');
  await page.screenshot({ path: 'artifacts/checklist-mobile.png', fullPage: true });
  results.checks.push('mobile sidebar and no page overflow');

  await page.locator('button.DocSearch-Button').click();
  await page.locator('#localsearch-input').fill('react.form');
  await expect(page.locator('.VPLocalSearchBox a[href*="react.form"]').first()).toBeVisible();
  await page.keyboard.press('Escape');
  results.checks.push('mobile search');
  if (errors.length || networkErrors.length) throw Error(JSON.stringify({ errors, networkErrors }));
  results.checks.push('no browser exceptions or failed local requests');
  await writeFile('artifacts/site-check-results.json', JSON.stringify(results, null, 2) + '\n');
  console.log(`Browser OK: ${results.checks.length} checks; base=${base}`);
} finally {
  if (browser) await browser.close();
  await new Promise(resolve => server.close(resolve));
}
