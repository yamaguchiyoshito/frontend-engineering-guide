---
title: "Web基礎"
description: "ブラウザがサーバーと通信して画面を表示するまでの仕組みを扱う要素技術です。HTTPの要求と応答、URL、Cookie、キャッシュの動作を理解し、通信の内容から不具合を切り分けられるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# Web基礎

**要素技術ID：** `web.basic`  
**領域：** [基礎領域](index.md)  
**評価対象：** HTTP、URL、ブラウザ、Cookie、キャッシュ

<!-- terms:start -->

**前提となる用語：** [ブラウザ](../../guide/glossary.md#ブラウザ)、[サーバー](../../guide/glossary.md#サーバー)、[HTTP](../../guide/glossary.md#http)、[リクエストとレスポンス](../../guide/glossary.md#リクエストとレスポンス)、[ステータスコード](../../guide/glossary.md#ステータスコード)、[URL](../../guide/glossary.md#url)、[Cookie](../../guide/glossary.md#cookie)、[キャッシュ](../../guide/glossary.md#キャッシュ)、[開発者ツール](../../guide/glossary.md#開発者ツール)

<!-- terms:end -->

ブラウザがサーバーと通信して画面を表示するまでの仕組みを扱う要素技術です。HTTPの要求と応答、URL、Cookie、キャッシュの動作を理解し、通信の内容から不具合を切り分けられるかを評価します。

## Lv0

ブラウザとサーバーの役割、URL、リクエストとレスポンスの関係を説明できず、通信内容の確認には手順ごとの指示が必要である。

## Lv1

基本的なHTTPメソッドとステータスコードの意味を説明し、手順に沿って開発者ツールで通信・Cookie・キャッシュの状態を確認できる。

## Lv2

画面表示やAPI呼び出しの通信を追跡し、URL、ヘッダー、ステータス、Cookie、キャッシュの設定から、標準的な通信不具合を切り分けて修正を確認できる。

## Lv3

リダイレクト、クロスオリジン通信、Cookieの送信条件、複数層のキャッシュが絡む問題を分析し、原因と影響範囲を説明して設定・実装を改善できる。

## Lv4

チームで使用する通信・Cookie・キャッシュの設計原則と診断手順を整備し、確認の自動化や教材として展開できる。他者の利用結果から不具合の再発や調査時間の改善を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [MDN：Webの仕組み](https://developer.mozilla.org/ja/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) — ブラウザとサーバーの通信の流れ
- [MDN：HTTP](https://developer.mozilla.org/ja/docs/Web/HTTP) — 要求と応答、ヘッダー、ステータスコードのリファレンス
- [MDN：HTTP Cookie](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Cookies) — Cookieの属性と送信条件
- [MDN：HTTPキャッシュ](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Caching) — ブラウザと中間キャッシュの動作
- [RFC 9110：HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — HTTPの意味論を定める標準仕様（英語）

**代表的なライブラリ・ツール**

- [Chrome DevTools：Networkパネル](https://developer.chrome.com/docs/devtools/network?hl=ja) — 通信内容とタイミングの確認
- [curl](https://curl.se/docs/) — コマンドラインからのHTTP要求と応答の確認

<!-- references:end -->
