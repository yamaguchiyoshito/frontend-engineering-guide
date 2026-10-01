---
title: "基本SEO"
description: "検索エンジンに公開ページを正しく巡回・索引登録させる要素技術です。タイトル、内部リンク、正規URL、サイトマップを設定し、重複URLや動的描画、移行時のリダイレクトの影響を調査できるかを評価します。"
titleTemplate: ":title | 要素技術 | 習熟度ガイド"
---

# 基本SEO

**要素技術ID：** `web.seo`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** HTML、セマンティックHTML

<!-- terms:start -->

**前提となる用語：** [SEO](../../guide/glossary.md#seo)、[セマンティックHTML](../../guide/glossary.md#セマンティックhtml)、[レンダリング](../../guide/glossary.md#レンダリング)、[Core Web Vitals](../../guide/glossary.md#core-web-vitals)

<!-- terms:end -->

検索エンジンに公開ページを正しく巡回・索引登録させる要素技術です。タイトル、内部リンク、正規URL、サイトマップを設定し、重複URLや動的描画、移行時のリダイレクトの影響を調査できるかを評価します。

::: start
「Google検索セントラル」のSEOスターターガイドで、検索エンジンがページを見つけて理解する仕組みを読みます。title、説明文（meta description）、見出しを整え、LighthouseのSEO監査を通せれば、Lv1の入口です。まず読む：[Google検索セントラル](https://developers.google.com/search/docs?hl=ja)
:::

## Lv0

検索エンジンの巡回・索引登録と検索結果表示の違いを説明できず、公開ページの基本設定の確認に支援が必要である。

## Lv1

手順に沿ってタイトル、説明文、見出し、リンクを設定し、公開ページの内容を確認できる。索引登録の可否に関する設定を支援の下で確認できる。

## Lv2

公開目的に合わせてタイトル、内部リンク、正規URL、サイトマップ、索引登録の制御を設定・確認できる。非公開情報のアクセス制御をSEO設定で代替しないことを説明できる。

## Lv3

重複URL、ページ分割、JavaScriptによる描画、移行時のリダイレクトなどが巡回・索引登録に与える影響を調査できる。原因に対応する改善を実施し、変化を継続して確認できる。

## Lv4

公開サイトのSEO要件、共通テンプレート、公開前の検査、運用指標を整備できる。コンテンツ担当者と運用を定着させ、索引登録上の問題や検索経由の利用状況から改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [Google検索セントラル](https://developers.google.com/search/docs?hl=ja) — 検索エンジン向けの公式ガイド
- [sitemaps.org：プロトコル](https://www.sitemaps.org/ja/protocol.html) — サイトマップの仕様
- [Google：robots.txtの概要](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=ja) — 巡回制御の設定

**代表的なライブラリ・ツール**

- [Google Search Console](https://search.google.com/search-console/about?hl=ja) — 索引登録状況と検索パフォーマンスの確認
- [Lighthouse](https://developer.chrome.com/docs/lighthouse?hl=ja) — SEO監査を含むページ診断

<!-- references:end -->
