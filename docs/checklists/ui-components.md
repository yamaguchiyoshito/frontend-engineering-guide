---
title: "UIコンポーネント"
description: "Webフロントエンド版DX Criteria 1-3「UIコンポーネント」（持続可能な技術スタック）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 開発ガイド"
---

# UIコンポーネント

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 1. 持続可能な技術スタック  
**小テーマ：** 1-3 UIコンポーネント

<!-- terms:start -->

**前提となる用語：** [コンポーネント](../guide/glossary.md#コンポーネント)、[Storybook](../guide/glossary.md#storybook)、[React](../guide/glossary.md#react)、[デザインシステムとデザイントークン](../guide/glossary.md#デザインシステムとデザイントークン)、[アクセシビリティ](../guide/glossary.md#アクセシビリティ)  
**関連する要素技術：** [コンポーネント設計](../skills/implementation/react.component-design.md)、[Storybook](../skills/implementation/storybook.basic.md)、[React実装](../skills/implementation/react.basic.md)、[スタイリング設計](../skills/implementation/frontend.styling.md)

<!-- terms:end -->

## 1-3-1：メトリクスの計測

広く共通化を意図しているUIコンポーネントがカタログ化されており、それに該当しないものも定期的（月ごと〜半年ごと）に整理し、改善している。

::: example
共通UIコンポーネントをカタログ化し、用途・入力項目・表示状態・使用例を参照できるようにしています。四半期ごとに、画面固有のコンポーネントも含めて重複・未使用・共通化候補を棚卸ししています。統合や廃止は利用箇所と移行方法を確認したうえで実施しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/233a23850a854c80839d863468efa64e)

## 1-3-2：学習と改善

UIコンポーネントの責務、再利用性、インターフェースに関するチーム内プラクティスを逐次共有し、定期的（月ごと〜半年ごと）に見直して改善している。

::: example
UIコンポーネントの責務、状態管理の置き場所、再利用の判断基準、公開インターフェースの設計方針を文書化しています。PRレビューで得た知見を随時追記し、具体的な実装例とともに共有しています。四半期ごとに実装とのずれを確認し、方針とコンポーネントを更新しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/9d433c2ae6ad4257aafc9d7eac2d9f9e)

## 1-3-3：プラクティス

コンポーネント指向なUIライブラリやフレームワーク（React, Vue.js, Angularなど）やWeb技術を使用している。

::: example
コンポーネント指向のUIフレームワークを使用し、表示・状態・イベントの境界を定めて画面を構築しています。共通部品と画面固有部品を区別し、各部品を単独で表示・検証できる構成にしています。採用フレームワークと基本的な実装方法を開発ガイドに記載しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/8bc5b812ba3d4a1290e5fcd076230a07)

## 1-3-4：アンチパターン

UIコンポーネントの設計パターンが開発者間で共有されておらず、コンポーネントの粒度をコントロールできていない（細かすぎ、大きすぎ）。

::: example
コンポーネントの設計パターンをチームで共有しており、粒度を各開発者の判断だけに任せていません。責務、変更理由、再利用範囲、テストのしやすさを基準に分割・統合をレビューしています。過度に細分化された部品や責務が集中した部品は、改善対象として管理しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/d8624cedad794b39a9d2b387394a20a7)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [React：Reactの流儀（日本語）](https://ja.react.dev/learn/thinking-in-react) — コンポーネントの分割と責務
- [Storybook：ドキュメント](https://storybook.js.org/docs) — カタログ化と説明の整備

**代表的なツール・サービス**

- [React](https://ja.react.dev/)（出典で言及） — コンポーネント指向のUIライブラリ
- [Vue.js](https://ja.vuejs.org/)（出典で言及） — コンポーネント指向のUIフレームワーク
- [Angular](https://angular.dev/)（出典で言及） — コンポーネント指向のUIフレームワーク
- [Storybook](https://storybook.js.org/) — UIコンポーネントのカタログ
- [Radix Primitives](https://www.radix-ui.com/primitives) — 責務を絞ったアクセシブルな部品。shadcn/uiの基盤
- [shadcn/ui](https://ui.shadcn.com/docs) — Radixを基盤にしたUI部品集
- [Tailwind CSS](https://tailwindcss.com/docs) — ユーティリティクラスによるスタイリング

<!-- references:end -->
