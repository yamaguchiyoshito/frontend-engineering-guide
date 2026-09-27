---
title: "スタイリング設計"
description: "コンポーネント指向の画面でスタイルを設計する要素技術です。ユーティリティクラス、デザイントークン、コンポーネントの見た目のバリエーション、ダークモード、既製UI部品のカスタマイズを扱い、共通のテーマを崩さずに画面を実装・変更できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# スタイリング設計

**要素技術ID：** `frontend.styling`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** CSS、レスポンシブ設計、コンポーネント設計

<!-- terms:start -->

**前提となる用語：** [CSS](../../guide/glossary.md#css)、[ユーティリティクラス](../../guide/glossary.md#ユーティリティクラス)、[デザインシステムとデザイントークン](../../guide/glossary.md#デザインシステムとデザイントークン)、[テーマとダークモード](../../guide/glossary.md#テーマとダークモード)、[コンポーネント](../../guide/glossary.md#コンポーネント)、[レスポンシブデザイン](../../guide/glossary.md#レスポンシブデザイン)

<!-- terms:end -->

コンポーネント指向の画面でスタイルを設計する要素技術です。ユーティリティクラス、デザイントークン、コンポーネントの見た目のバリエーション、ダークモード、既製UI部品のカスタマイズを扱い、共通のテーマを崩さずに画面を実装・変更できるかを評価します。

::: start
Tailwind CSS公式の「Styling with utility classes」で、クラスを組み合わせて見た目を指定する考え方と、テーマの値がどこで決まるかを読みます。既存のボタンについて、通常・強調・無効の3種類をテーマの色だけで表現し、画面幅に応じて余白を変えられれば、Lv1の入口です。まず読む：[Tailwind CSS：Styling with utility classes](https://tailwindcss.com/docs/styling-with-utility-classes)
:::

## Lv0

ユーティリティクラス、テーマの値、コンポーネントのバリエーションの関係を説明できず、見た目の変更に手順ごとの指示が必要である。

## Lv1

既存のテーマとクラスの例に沿って、色、余白、文字、状態ごとの見た目を変更できる。新しいバリエーションの追加やダークモードへの対応には支援が必要である。

## Lv2

デザイントークンに沿ってコンポーネントの状態とバリエーションを実装し、ダークモードと画面幅に応じた表示を共通テーマを崩さずに実装できる。既製のUI部品をテーマに合わせて調整し、指定と実際の見た目の差を自分で検証・修正できる。

## Lv3

トークンの階層（基礎値と意味付けされた値）、クラスの重複や競合、ユーティリティとCSS Modulesの使い分け、部品ごとの例外を分析して設計できる。デザインツールとコードの差異を見つけ、影響範囲を抑えてテーマと部品を段階的に改善できる。

## Lv4

デザイントークンの管理方法、デザインツールとの同期、スタイルの規約、共通部品のバリエーション体系、変更時の確認手順を整備できる。デザイナーと開発者の運用を定着させ、見た目の不整合や変更工数の改善を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [Tailwind CSS：Styling with utility classes](https://tailwindcss.com/docs/styling-with-utility-classes) — ユーティリティクラスの考え方
- [Tailwind CSS：Theme variables](https://tailwindcss.com/docs/theme) — テーマの値の定義と参照
- [Tailwind CSS：Dark mode](https://tailwindcss.com/docs/dark-mode) — ダークモードの切り替え
- [shadcn/ui：Theming](https://ui.shadcn.com/docs/theming) — CSS変数によるテーマの調整
- [Design Tokens Format Module](https://tr.designtokens.org/format/) — デザイントークンの標準形式（英語）
- [Figma：バリアブルのガイド](https://help.figma.com/hc/ja/articles/15339657135383) — デザイントークンをFigmaで一元管理

**代表的なライブラリ・ツール**

- [Tailwind CSS](https://tailwindcss.com/docs) — ユーティリティクラスによるスタイリング
- [shadcn/ui](https://ui.shadcn.com/docs) — Radixを基盤にした複製して使うUI部品集
- [class-variance-authority](https://cva.style/docs) — コンポーネントのバリエーション定義
- [Style Dictionary](https://styledictionary.com/) — デザイントークンから各種形式への変換
- [CSS Modules](https://github.com/css-modules/css-modules) — コンポーネント単位のCSSのスコープ化

<!-- references:end -->
