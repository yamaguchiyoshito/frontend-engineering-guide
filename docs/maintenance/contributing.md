---
title: "編集・検証・公開手順"
description: "正本のファイル、ローカルでの確認手順、Pull Requestでの確認、mainへのマージによる公開、公開済みの版への復旧。"
---

# 編集・検証・公開手順

## 編集するファイル

| 変更内容 | 正本 |
| :--- | :--- |
| 使い方・判定方法 | `docs/guide/*.md` |
| 習熟度の定義 | `docs/skills/<領域>/<要素技術ID>.md` |
| チェック項目・回答例 | `docs/checklists/<小テーマ>.md`（項目文は出典のとおり。回答例のみ編集） |
| 記録書式 | `docs/templates/*.md` のテンプレート欄 |
| 要素技術・小テーマの参考リンク | `build/references.json`（`docs:sync` で各ページへ展開） |
| ページの追加・順序・分類 | `build/document-map.json` |
| 公開版 | `package.json` のversion・このサイトの改訂履歴 |

一覧ページの `catalog` マーカー内、サイトのHTML、ダウンロードファイルは自動生成します。本文・書式の正本を変更してから生成してください。

## ローカルで確認する

Node.js 24とPython 3.12以降を使用します。

```bash
npm ci
npm run docs:sync
npm run docs:check
npm run docs:dev
```

公開成果物を確認する場合は、次を実行します。

```bash
npm run docs:build
npx playwright install chromium
npm run test:site
npm run docs:preview
```

`docs:build` は構造検査、単一文書・書式生成、静的HTML生成を行います。`test:site` は公開用HTMLのリンク・アンカー・ダウンロードとブラウザでの検索・表示を確認します。

## Pull Requestで確認する

変更理由、対象要素技術ID・項目ID、既存評価への影響、再評価の要否を記載します。文言変更でも到達状態が変わる場合は、適用版と移行方針を明記します。

公開リポジトリのIssueやPRには基準の改善提案だけを記載し、実際の個人評価・案件記録は記載しません。

## 確定版を公開する

GitHubの一般公開リポジトリを使用します。初回だけ **Settings → Pages → Build and deployment → Source: GitHub Actions** を選びます。Enterpriseは必要ありません。

`github-pages` 環境の公開元は `main` のみで構いません。**Settings → Environments → github-pages** の初期設定のまま使用できます。

1. `npm version patch --no-git-tag-version` などでバージョンとlockfileを更新します。
2. 改訂履歴に同じ版の項目を追加し、PRの検査（**Validate documentation**）が通ったことを確認します。
3. PRを `main` にマージします。マージを契機に **Publish GitHub Pages** がビルド・検証・公開を行います。
4. Actionsの実行が成功したら、表示された公開URLを開いて版と表示を確認します。

`main` にマージした内容がそのまま公開されます。PRの段階では検査だけを行い、公開サイトを変更しません。

## 公開済みの版へ戻す

`main` で該当する変更を取り消す（revert）PRを作成し、検査を通してマージします。マージにより取り消し後の内容が公開されます。ビルドの再実行だけが必要な場合は、Actionsの **Publish GitHub Pages → Run workflow** を `main` から実行します。

## 公開先とURL

標準URLは `https://<owner>.github.io/<repository>/` です。公開処理がGitHub Pagesの設定からベースパスとオリジンを取得するため、リポジトリ名を変更してもソース内のURL修正は不要です。独自ドメインを使う場合もPagesの設定を先に更新します。

詳しい初回pushの手順とディレクトリ構成は、リポジトリのREADME・ARCHITECTUREに記載しています。
