# フロントエンド習熟度ガイド

一般公開のGitHub Pagesで読む、要素技術の習熟度評価とチーム改善の文書です。開発プロセスの手順書ではなく、個人の習熟度（Lv0〜Lv4）とチームの取り組みを確認する基準と、その評価の進め方を示します。

- **要素技術：** 4領域・31の要素技術について、Lv0〜Lv4の到達状態を155の定義で示します。
- **チームチェックリスト：** 日本CTO協会 Webフロントエンド版DX Criteriaの100項目（5つの大テーマ・25の小テーマ・4つの観点）を出典の分類と文面で収録し、架空の回答例を添えます。
- **使い方と書式：** 評価の手順、4種類の空の記録書式、架空の記入例を収録します。
- **公開サイト：** 85ページ、日本語全文検索、単一Markdownと書式のダウンロードに対応します。習熟度マトリクスでは、Lvのセルを選んで自己評価をブラウザ内に記録し、集計をページ内で確認できます。チームチェックでは、小テーマごとのページまたは100項目を1ページに並べた回答シートで、項目ごとに回答と評価記述を記録し、出典の配点（はい 1点、でも 0.5点、いいえ 0点、アンチパターンは逆転）で小テーマ別・全体の得点を表示します。

まず [ガイドの全体像](docs/guide/overview.md) を読み、[要素技術](docs/skills/index.md)・[チームチェック](docs/checklists/index.md) を参照してください。詳細な構成は [ARCHITECTURE.md](ARCHITECTURE.md)、実行した検証は [VALIDATION.md](VALIDATION.md) に記載しています。

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
| `docs:check` | 85ページ、31の要素技術、155定義、100項目、判定、内部参照、用語集の参照を検査 |
| `docs:downloads` | 単一Markdown、空の4書式、ZIP、生成元・SHA-256を生成 |
| `docs:build` | 文書検査・ダウンロード生成・サイトビルド |
| `test:site` | 全HTMLのリンク・アンカーとブラウザの検索・表示・ダウンロード、マトリクスの自己評価の保存、チームチェックの回答と配点、目次のコンパクト表示を検査 |
| `check:migration` | 移行ベースライン（原稿1.1の140定義と1.3.0で追加した15定義、100項目）から変わっていないことを照合 |
| `check:links` | 要素技術・小テーマページの参考リンク（`build/references.json`）と学習コンテンツ（`build/learning.json`）の到達確認。週次のワークフローでも実行 |

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

チームチェックリストの原文は、一般社団法人日本CTO協会が公開する [Webフロントエンド版DX Criteria（v202402）](https://dxcriteria.cto-a.org/frontend) です。分類と文面は出典に従い、回答例と28の要素技術の定義は本リポジトリで追加した内容です。詳細は [出典と追加した内容](docs/maintenance/sources.md)、変更履歴は [改訂履歴](docs/maintenance/changelog.md) を参照してください。

## Agent Skill：評価の下書き

`.claude/skills/assessment-draft/` に、利用者が指定したリポジトリの状態とGit履歴から、個人の習熟度評価（31の要素技術 × Lv0〜Lv4）とチームチェック（100項目）の下書きを根拠付きで作る Agent Skill を同梱しています。

- このリポジトリを Claude Code で開くとプロジェクトのスキルとして自動で使えます。他の場所で使うには `.claude/skills/assessment-draft` を `~/.claude/skills/` にコピーします。
- 依頼の例：「`~/work/shop-front` について、山田さんの個人評価とチームチェックの下書きを作って（直近12か月）」
- 根拠の収集は同梱の `scripts/collect_evidence.py`（Python 3.9以降とgitのみ、読み取り専用、ネットワーク不使用）が行い、判定は手順書 `SKILL.md` と対応表 `references/` に従います。要素技術の定義と項目カタログ（`references/skills.json`、`references/checklist-items.json`）は `docs:sync` で本書から生成します。
- 出力は本書の「Markdownでコピー」と同じ書式の Markdown と、ページの保存形式と互換の JSON です。下書きは仮説であり、面談やチームのレビューで根拠を確認してから記録書式へ転記します。

## ライセンス

本リポジトリの内容（文書、記録書式、回答例、スクリプト、サイト設定）は、[クリエイティブ・コモンズ 表示—継承 4.0 国際（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) で提供します。全文は [LICENSE](LICENSE) にあります。出典であるWebフロントエンド版DX Criteriaも同じライセンスで提供されており、その著作権は一般社団法人日本CTO協会に帰属します。

利用・再配布・改変の際は、本ガイドと出典の名称、URL、ライセンスを表示し、改変した派生物も CC BY-SA 4.0 で提供してください。
