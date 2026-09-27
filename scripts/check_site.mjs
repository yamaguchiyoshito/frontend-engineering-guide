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
const results = { base, pages: 79, definitions: 140, checklistItems: 100, checks: [] };
let browser;
try {
  browser = await chromium.launch({ headless: true, ...(process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH, args: JSON.parse(process.env.PLAYWRIGHT_CHROMIUM_ARGS || '["--no-sandbox","--disable-dev-shm-usage"]') } : {}) });
  results.browser = browser.version();
  const page = await browser.newPage({ viewport: { width: 1440, height: 1050 } });
  const errors = []; const networkErrors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('response', response => { if (response.url().startsWith(origin) && response.status() >= 400) networkErrors.push(response.url()); });
  await page.goto(url);
  await expect(page.locator('h1')).toHaveText('フロントエンド開発ガイド');
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
  await expect(page.locator('.mermaid svg').first()).toBeVisible({ timeout: 15000 });
  results.checks.push('mermaid sequence diagram renders');

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
