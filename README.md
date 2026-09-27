# フロントエンド開発ガイド

一般公開のGitHub Pagesで読む、スキル評価とチーム改善の文書です。

- **スキル定義：** 4領域・28スキルについて、Lv0〜Lv4の到達状態を140の定義で示します。
- **チームチェックリスト：** 日本CTO協会 Webフロントエンド版DX Criteriaの100項目（5つの大テーマ・25の小テーマ・4つの観点）を原典の分類と文面で収録し、望ましい回答と架空の回答例を添えます。
- **使い方と書式：** 評価の手順、4種類の空の記録書式、架空の記入例を収録します。
- **公開サイト：** 76ページ、日本語全文検索、単一Markdownと書式のダウンロードに対応します。

まず [ガイドの全体像](docs/guide/overview.md) を読み、[スキル定義](docs/skills/index.md)・[チームチェック](docs/checklists/index.md) を参照してください。詳細な構成は [ARCHITECTURE.md](ARCHITECTURE.md)、実行した検証は [VALIDATION.md](VALIDATION.md) に記載しています。

## ローカルで読む

Node.js **24.19.0**（`.nvmrc`）、Python **3.12以降**を使用します。

```bash
npm ci
npm run docs:dev
```

表示されたローカルURLの `/frontend-engineering-guide/` を開きます。ホスト名やリポジトリ名をソースに書き込む必要はありません。

## GitHubへ初回登録する

1. GitHubで、任意の所有者の下に **Public** リポジトリを新規作成します。推奨名は `frontend-engineering-guide` です。README等の初期ファイルは作成しません。
2. このフォルダー内で次を実行します。`YOUR_OWNER` は実際のアカウント・組織名に置き換えてください。

```bash
git init -b main
git add .
git commit -m "Add public frontend engineering guide"
git remote add origin https://github.com/YOUR_OWNER/frontend-engineering-guide.git
git push -u origin main
```

3. **Settings → Pages → Build and deployment → Source** で **GitHub Actions** を選択します。
4. **Settings → Environments → github-pages** の公開元制限は `main` のみで問題ありません。他のブランチからは公開しません。

`main` へのpushを契機に **Publish GitHub Pages** がビルド・ブラウザ検証後に公開します。初回はpush直後に実行され、以後はPRのマージごとに実行されます。公開URLはActionsのdeploymentまたはSettings → Pagesに表示されます。標準URLは `https://YOUR_OWNER.github.io/frontend-engineering-guide/` です。

GitHub Freeでは公開リポジトリからPagesを公開できます。公開サイトにログインは不要です。[公式仕様](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

## 検査と生成

```bash
npm run docs:sync
npm run docs:build
npx playwright install --with-deps chromium
npm run test:site
npm run docs:preview
```

| コマンド | 処理 |
| :--- | :--- |
| `docs:sync` | 文書マップから一覧ページのリンク・表を同期 |
| `docs:check` | 76ページ、28スキル、140定義、100項目、判定、内部参照を検査 |
| `docs:downloads` | 単一Markdown、空の4書式、ZIP、生成元・SHA-256を生成 |
| `docs:build` | 文書検査・ダウンロード生成・サイトビルド |
| `test:site` | 全HTMLのリンク・アンカーとブラウザの検索・表示・ダウンロードを検査 |
| `check:migration` | 原稿1.1から140定義・100項目が変わっていないことを照合 |

`check:migration` は今回の移行確認用です。今後の意図した定義改訂では差分になるため、通常CIには含めていません。

生成物は `docs/.vitepress/dist/`（公開サイト）、`dist/frontend-handbook.md`（単一文書）、`docs/public/downloads/`（配布ファイル）です。生成物と `node_modules` はコミットしません。

## URLを変えて検証する

```bash
SITE_BASE_PATH=/ npm run docs:build
npm run test:site
SITE_BASE_PATH=/preview-repository/ npm run docs:build
npm run test:site
```

本番では `configure-pages` が取得したベースパスとオリジンを使います。ユーザーサイトや独自ドメインにも同じ生成処理を使えます。独自ドメインはGitHub Pages側で先に設定してください。

## 改訂・再公開

編集内容は [編集・検証・公開手順](docs/maintenance/contributing.md) に従ってPRで確認します。PRでは **Validate documentation** が検査だけを行います。`main` へマージすると **Publish GitHub Pages** が同じ検査を通してから公開します。`main` の内容がそのまま公開サイトです。

旧版へ戻すには、`main` で該当する変更を取り消す（revert）PRをマージします。公開の再実行だけが必要な場合は **Publish GitHub Pages → Run workflow** を `main` から実行します。同時の公開要求は直列に処理されます。

## 公開する内容

このリポジトリは基準・使い方・空の書式・架空の回答例を管理します。記入済みの個人評価、社内URL、案件情報は所属組織の管理先へ保存します。サイトに入力・保存・認証の機能はありません。検索は配信済みの索引をブラウザ内で検索します。

チームチェックリストの原文は、一般社団法人日本CTO協会が公開する [Webフロントエンド版DX Criteria（v202402）](https://dxcriteria.cto-a.org/frontend) です。分類と文面は原典に従い、項目No.、望ましい回答、回答例、28スキルの定義は本リポジトリで追加した内容です。詳細は [出典と追加した内容](docs/maintenance/sources.md)、変更履歴は [改訂履歴](docs/maintenance/changelog.md) を参照してください。

## ライセンス

本リポジトリの内容（文書、記録書式、回答例、スクリプト、サイト設定）は、[クリエイティブ・コモンズ 表示—継承 4.0 国際（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) で提供します。全文は [LICENSE](LICENSE) にあります。原典であるWebフロントエンド版DX Criteriaも同じライセンスで提供されており、その著作権は一般社団法人日本CTO協会に帰属します。

利用・再配布・改変の際は、本ガイドと原典の名称、URL、ライセンスを表示し、改変した派生物も CC BY-SA 4.0 で提供してください。
