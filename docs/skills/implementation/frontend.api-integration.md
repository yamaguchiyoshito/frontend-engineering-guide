---
title: "REST API連携"
description: "REST APIと連携して画面を動かす要素技術です。API仕様から要求と応答を実装し、読み込み中、空データ、失敗、認証切れを扱い、複数APIの依存や部分失敗、仕様変更に対応できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# REST API連携

**要素技術ID：** `frontend.api-integration`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** 非同期処理、TypeScript

<!-- terms:start -->

**前提となる用語：** [API](../../guide/glossary.md#api)、[REST API](../../guide/glossary.md#rest-api)、[JSON](../../guide/glossary.md#json)、[HTTP](../../guide/glossary.md#http)、[非同期処理](../../guide/glossary.md#非同期処理)、[OpenAPI](../../guide/glossary.md#openapi)、[モック](../../guide/glossary.md#モック)

<!-- terms:end -->

REST APIと連携して画面を動かす要素技術です。API仕様から要求と応答を実装し、読み込み中、空データ、失敗、認証切れを扱い、複数APIの依存や部分失敗、仕様変更に対応できるかを評価します。

::: start
MDNの「Fetch API」で、要求の送り方と応答の読み方を確認します。公開APIから一覧を取得して画面に表示し、読み込み中とエラーの表示を分けられれば、Lv1の入口です。まず読む：[MDN：Fetch API](https://developer.mozilla.org/ja/docs/Web/API/Fetch_API)
:::

## Lv0

API仕様のURL、メソッド、要求・応答、ステータスを読み取れず、呼び出しと表示の実装に手順ごとの指示が必要である。

## Lv1

用意された仕様と例に沿ってAPIを呼び出し、応答を画面に表示できる。パラメーターや失敗時の扱いは支援を受けて実装できる。

## Lv2

API仕様から要求・応答を実装し、読み込み中、空データ、失敗、認証切れを画面で扱える。モックと実APIの双方で動作を確認し、通信内容から通常の不整合を修正できる。

## Lv3

複数APIの依存、ページ分割、部分失敗、キャンセル、仕様変更を設計に反映できる。再試行してよい操作を判断し、バックエンドとエラー契約や互換性を調整できる。

## Lv4

APIクライアント、型生成・契約確認、共通エラー処理、通信の観測方法を整備できる。フロントエンドとバックエンドの双方へ展開し、連携不具合と仕様変更時の手戻りを減らせる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [MDN：Fetch API](https://developer.mozilla.org/ja/docs/Web/API/Fetch_API) — HTTP要求のリファレンス
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — REST APIの仕様記述形式（英語）
- [MDN：CORS](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/CORS) — オリジン間要求の仕組み

**代表的なライブラリ・ツール**

- [TanStack Query](https://tanstack.com/query) — 取得、キャッシュ、再試行、更新の管理
- [Mock Service Worker](https://mswjs.io/) — ネットワーク層でのAPIモック
- [openapi-typescript](https://openapi-ts.dev/) — OpenAPIからの型生成
- [orval](https://orval.dev/) — OpenAPIからのクライアントと型の生成
- [openapi-zod-client](https://github.com/astahmer/openapi-zod-client) — OpenAPIからZodスキーマとクライアントを生成

<!-- references:end -->
