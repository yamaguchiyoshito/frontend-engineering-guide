# 構成と公開設計

文書の正本は `docs/` のMarkdownです。同じ正本からGitHub Pagesのサイトと単一Markdownを生成します。以前の限定公開・Enterprise想定を変更し、**公開リポジトリと一般公開のPages** を採用しています。

## ディレクトリごとの責任

| パス | 内容・責任 |
| :--- | :--- |
| `README.md` | 初回登録、公開、ローカル実行、ライセンスの入口 |
| `LICENSE` | CC BY-SA 4.0 の全文。リポジトリ全体に適用 |
| `ARCHITECTURE.md` | ページ構成と生成・公開設計 |
| `CHANGELOG.md` | 改訂履歴の正本 `docs/maintenance/changelog.md` への入口。編集手順は `docs/maintenance/contributing.md` |
| `docs/index.md` | 読む順序と目的別の入口 |
| `docs/guide/` | 個人・チームの評価手順と改善方法 |
| `docs/skills/<領域>/<ID>.md` | 1スキル1ファイル、Lv0〜Lv4の正本 |
| `docs/checklists/<小テーマ>.md` | 原典の1小テーマ1ファイル、各4項目の正本 |
| `docs/templates/` | 記入説明と空のテンプレートの正本 |
| `docs/examples/` | 架空の記入例 |
| `docs/maintenance/` | 運用・改訂・出典 |
| `docs/downloads.md` | 生成した配布物の入口 |
| `docs/.vitepress/` | サイト設定、ナビゲーション、日本語検索、テーマ |
| `docs/public/assets/` | 公開する静的アセット |
| `docs/public/downloads/` | ビルド時に生成する配布物。Git管理対象外 |
| `build/document-map.json` | 全ページのパス・タイトル・分類・順序 |
| `build/migration-baseline.json` | 原稿1.1の移行照合用ハッシュ。本文の複製は持たない |
| `scripts/` | 構造検査、一覧同期、配布物生成、HTML・ブラウザ検証 |
| `.github/workflows/docs.yml` | PRの検査。ルート・サブディレクトリの2構成 |
| `.github/workflows/pages.yml` | `main` へのpushを契機に、ビルド、ブラウザ確認、Pagesへの公開 |
| `.github/pull_request_template.md` | 変更理由・評価影響・検証結果の記録 |
| `package.json` / `package-lock.json` | 文書版、実行コマンド、固定した依存関係 |
| `.nvmrc` | 開発・CIで使うNode.jsの版 |
| `dist/` / `artifacts/` | 単一文書と検査結果。Git管理対象外 |

## ページ構成

| ページ群 | ページ数 | 入口 |
| :--- | ---: | :--- |
| ホーム | 1 | `docs/index.md` |
| 使い方ガイド | 4 | `docs/guide/overview.md` |
| スキル一覧 | 1 | `docs/skills/index.md` |
| 領域一覧 | 4 | `docs/skills/<領域>/index.md` |
| スキル個別定義 | 28 | `docs/skills/<領域>/<ID>.md` |
| チェックリスト一覧 | 1 | `docs/checklists/index.md` |
| 小テーマ別チェックリスト | 25 | `docs/checklists/<小テーマ>.md` |
| 書式一覧・書式 | 5 | `docs/templates/index.md` |
| 記入例一覧・記入例 | 2 | `docs/examples/index.md` |
| 運用・改訂 | 4 | `docs/maintenance/index.md` |
| ダウンロード | 1 | `docs/downloads.md` |
| **合計** | **76** | 404ページとダウンロードファイルを除く |

全ファイルの対応は `build/document-map.json` で管理します。4領域のディレクトリは `foundation`、`applied-foundation`、`implementation`、`quality` です。スキル分類に「レベル」は使用せず、習熟度だけをLv0〜Lv4で表します。

## 閲覧経路とURL

- 上部メニュー：使い方、スキル定義、チームチェック、書式・記入例、運用・改訂。ダウンロードを補助リンクとして配置。
- サイドバー：開いているページ群に対応。28スキルは領域ごと、25の小テーマは原典の5つの大テーマごとに折りたたむ。
- 初めて読む順序：全体像 → 個人評価 → チーム確認 → 改善 → 詳細定義 → 書式。前後リンクも文書マップから生成。
- 各ページ：見出し目次、版、本文、前後ページへのリンク。
- ページURL：`index.md` は末尾 `/`、他は `.html`。例：`skills/implementation/react.form.html#lv3`、`checklists/security.html#c029`。
- 原稿中の内部リンクは相対Markdownリンクで記載し、GitHubの閲覧とPagesの両方で辿れるようにする。

## 正本と生成物

`document-map.json` は構造情報のみを持ち、習熟度定義・回答例は各Markdownに一度だけ記載します。一覧の自動生成箇所は `catalog` コメントで区切ります。変更時に `docs:sync` を実行し、同期漏れをCIで検出します。

単一Markdownでは、各ページ・見出しに一意のアンカーを生成し、ページ間の参照を文書内参照へ変換します。コードブロック内の記入用見出しは変換しません。全アンカーの存在を生成時に確認します。

書式ダウンロードは各ページの `template` コメント内を抽出します。4書式の個別MarkdownとZIPを生成し、版・コミット・生成日時を添えます。配布マニフェストにはサイズとSHA-256を記録します。

`docs/public/**` はMarkdownページの走査対象から除き、生成した配布Markdownが重複した閲覧ページ・検索結果にならないようにします。

## 技術構成

- VitePress **1.6.4** の安定版と標準テーマを使用。
- Viteは **6.4.3** にoverrideで固定。VitePress既定の旧版に残る開発サーバー関連の既知問題を避け、サイト生成・表示を検証。
- 依存はpackage-lock.jsonに固定し、CIでは `npm ci` を使用。
- 日本語は文字と連続2文字の組で索引化する。Node.jsとブラウザ間の辞書差異を避け、索引側と検索側へ同じtokenize関数を適用する。英数字の区切りは固定し、`react.form`、`C029`、`029` を保持する。
- 検索はVitePressのローカル検索。外部の検索サービスやAPIキーを使用しない。
- 明暗表示、キーボード操作、モバイル目次・検索に対応。外部フォントや解析タグは追加しない。

## 検査と公開の境界

PRの検査は `contents: read` で実行し、公開権限を持ちません。ルート `/` とプロジェクトパス `/preview-repository/` の両方で、文書の整合、HTMLの参照、検索、ダウンロード、モバイル表示を確認します。

公開ワークフローは `main` へのpushを対象とし、マージされた内容をそのまま公開します。ビルドジョブは読み取り権限で動き、文書検査とブラウザ検証を通過したPages artifactだけをデプロイジョブが公開します。デプロイジョブにのみ `pages: write` と `id-token: write` を付けます。

公開先のbase pathとoriginはGitHub Pagesの設定から取得します。コードに所有者名を固定しません。同時公開を直列化します。旧版へ戻す場合は `main` で変更を取り消し、手動実行は `main` の再公開に限ります。

GitHub上の設定と最初のpushはREADMEに記載しています。配布時点で特定のGitHubリポジトリへの登録や公開は行っていません。
