---
title: "セマンティックHTML"
description: "画面の情報構造を意味に沿ったHTMLで表現する要素技術です。見出し、ランドマーク、リスト、表、フォームを目的に合わせて選び、見た目と意味構造の不一致が操作や読み上げに与える影響を判断できるかを評価します。"
titleTemplate: ":title | 要素技術 | 習熟度ガイド"
---

# セマンティックHTML

**要素技術ID：** `html.semantic`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** HTML

<!-- terms:start -->

**前提となる用語：** [HTML](../../guide/glossary.md#html)、[セマンティックHTML](../../guide/glossary.md#セマンティックhtml)、[DOM](../../guide/glossary.md#dom)、[アクセシビリティ](../../guide/glossary.md#アクセシビリティ)、[支援技術とスクリーンリーダー](../../guide/glossary.md#支援技術とスクリーンリーダー)

<!-- terms:end -->

画面の情報構造を意味に沿ったHTMLで表現する要素技術です。見出し、ランドマーク、リスト、表、フォームを目的に合わせて選び、見た目と意味構造の不一致が操作や読み上げに与える影響を判断できるかを評価します。

::: start
MDNの「HTML要素リファレンス」で、header、nav、main、article、section、footerなど意味を表す要素を確認し、自分のページの各領域に当てはめます。開発者ツールのアクセシビリティツリーで、見出しの階層と領域が意図どおりに読まれることを確認できれば、Lv1の入口です。まず読む：[MDN：HTML要素リファレンス](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements)
:::

## Lv0

見た目と要素の意味の違いを説明できず、見出し、ナビゲーション、本文、ボタンなどの選択に手順ごとの指示が必要である。

## Lv1

例や支援に沿って見出しの階層、主要領域、リンクとボタンを使い分け、要素を選んだ基本的な理由を説明できる。

## Lv2

画面の情報構造と操作目的から要素を選び、見出し、ランドマーク、リスト、表、フォームを意味に沿って実装できる。DOMと読み上げ順序を確認できる。

## Lv3

複雑な画面や共通コンポーネントで、見た目と意味構造の不一致を特定し、操作・読み上げへの影響を説明できる。適切なHTMLを優先して構造を改善できる。

## Lv4

画面・コンポーネントの意味構造に関する共通パターンとレビュー基準を整備し、設計・実装に適用できる。他者による利用と検証を通じて構造上の不具合を減らせる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [MDN：HTML要素リファレンス](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements) — 各要素の意味と使い方
- [HTML Living Standard：セクションと見出し](https://html.spec.whatwg.org/multipage/sections.html) — 文書構造の仕様（英語）
- [ARIA in HTML](https://www.w3.org/TR/html-aria/) — HTML要素に許可されるARIAロールの対応表（英語）
- [web.dev：Learn HTML（セマンティクス）](https://web.dev/learn/html/semantic-html?hl=ja) — 意味構造の考え方

**代表的なライブラリ・ツール**

- [W3C Markup Validation Service](https://validator.w3.org/nu/) — 構造と入れ子の検査
- [Chrome DevTools：アクセシビリティツリー](https://developer.chrome.com/docs/devtools/accessibility/reference?hl=ja) — 支援技術に伝わる構造の確認

<!-- references:end -->
