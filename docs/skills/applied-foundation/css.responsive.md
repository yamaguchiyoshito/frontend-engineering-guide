---
title: "レスポンシブ設計"
description: "画面幅、向き、文字量、操作方法の違いに応じてレイアウトを設計する要素技術です。コンテンツの優先順位から表示の切り替えを決め、固定値に依存しない実装へ改善できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# レスポンシブ設計

**要素技術ID：** `css.responsive`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** CSS

<!-- terms:start -->

**前提となる用語：** [CSS](../../guide/glossary.md#css)、[レスポンシブデザイン](../../guide/glossary.md#レスポンシブデザイン)、[FlexboxとGrid](../../guide/glossary.md#flexboxとgrid)、[開発者ツール](../../guide/glossary.md#開発者ツール)

<!-- terms:end -->

画面幅、向き、文字量、操作方法の違いに応じてレイアウトを設計する要素技術です。コンテンツの優先順位から表示の切り替えを決め、固定値に依存しない実装へ改善できるかを評価します。

::: start
MDNの「レスポンシブデザイン」で、メディアクエリと相対的な単位の使い方を読みます。開発者ツールのデバイスモードで幅を変え、一つの画面がスマートフォンの幅とPCの幅で崩れずに並び替わる状態を作れれば、Lv1の入口です。まず読む：[MDN：レスポンシブデザイン](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)
:::

## Lv0

画面幅や文字量によってレイアウトが変わる理由を説明できず、複数の表示幅への対応に手順ごとの指示が必要である。

## Lv1

指定されたブレークポイントと例に沿ってレイアウトを切り替え、指定幅での表示崩れを確認・修正できる。

## Lv2

コンテンツ量と操作要件からレイアウトの切り替えを設計し、複数の画面幅・向き・文字量で主要操作が利用できるよう実装・確認できる。

## Lv3

大きな表、長い翻訳文、ズーム、タッチ操作などの制約を踏まえ、情報の優先順位と代替表示を設計できる。幅の固定値に依存する実装を分析・改善できる。

## Lv4

対応範囲、ブレークポイントの判断基準、レイアウト部品、検証パターンを共通化できる。チームへの展開後に、端末差による不具合や確認工数の改善を評価できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [MDN：レスポンシブデザイン](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) — メディアクエリと流動的なレイアウトの入門
- [MDN：コンテナクエリ](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_containment/Container_queries) — 親要素の大きさに応じたスタイル
- [web.dev：Learn Responsive Design](https://web.dev/learn/design?hl=ja) — レスポンシブ設計の学習コース

**代表的なライブラリ・ツール**

- [Chrome DevTools：デバイスモード](https://developer.chrome.com/docs/devtools/device-mode?hl=ja) — 画面幅と端末の模擬表示
- [Can I use](https://caniuse.com/) — ブラウザ対応状況の確認

<!-- references:end -->
