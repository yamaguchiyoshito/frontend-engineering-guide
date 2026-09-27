---
title: "CSS"
description: "CSSで画面の見た目とレイアウトを実装する要素技術です。セレクタ、カスケード、ボックスモデル、FlexboxやGridを理解し、表示の崩れを分析して保守しやすく修正できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# CSS

**要素技術ID：** `css.basic`  
**領域：** [基礎領域](index.md)  
**評価対象：** セレクタ、ボックスモデル、レイアウト

CSSで画面の見た目とレイアウトを実装する要素技術です。セレクタ、カスケード、ボックスモデル、FlexboxやGridを理解し、表示の崩れを分析して保守しやすく修正できるかを評価します。

## Lv0

セレクタ、余白、サイズ、ボックスモデルの基本を説明できず、指定された見た目への変更に手順ごとの指示が必要である。

## Lv1

例や支援に沿って、色、文字、余白、幅・高さを変更し、単純な横並び・縦並びのレイアウトを作成できる。

## Lv2

カスケード、継承、詳細度を踏まえ、FlexboxやGridなどで標準的な画面を実装できる。開発者ツールで適用スタイルを確認し、重なりやはみ出しを修正できる。

## Lv3

複数のスタイルが競合する画面や複雑なレイアウトで、サイズ計算、配置、積み重なりの問題を分析できる。影響範囲を抑えて修正し、保守しやすい構造へ改善できる。

## Lv4

スタイルの責任範囲、命名、共通値、例外の扱いをチームの規約と共通部品にできる。複数画面への適用を支援し、重複や表示不具合、変更工数の改善を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [MDN：CSS](https://developer.mozilla.org/ja/docs/Web/CSS) — プロパティとセレクタのリファレンス
- [MDN：CSSの学習](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Styling_basics) — カスケード、ボックスモデル、レイアウトの入門
- [MDN：Flexbox](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/CSS_layout/Flexbox) — 一次元レイアウトの解説
- [MDN：グリッド](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/CSS_layout/Grids) — 二次元レイアウトの解説
- [web.dev：Learn CSS](https://web.dev/learn/css?hl=ja) — CSSの体系的な学習コース

**代表的なライブラリ・ツール**

- [Chrome DevTools：CSSの検査](https://developer.chrome.com/docs/devtools/css?hl=ja) — 適用スタイルとボックスモデルの確認
- [Stylelint](https://stylelint.io/) — CSSの静的検査
- [PostCSS](https://postcss.org/) — CSSの変換とプラグイン基盤
- [Tailwind CSS](https://tailwindcss.com/docs) — ユーティリティクラスによるスタイリング

<!-- references:end -->
