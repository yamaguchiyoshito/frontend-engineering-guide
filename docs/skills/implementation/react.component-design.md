---
title: "コンポーネント設計"
description: "コンポーネントの責務と境界を設計する要素技術です。表示、業務処理、状態の役割を分け、利用側が理解できるpropsとイベントを定め、共通化の範囲と拡張性を判断できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# コンポーネント設計

**要素技術ID：** `react.component-design`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** React、UI実装

コンポーネントの責務と境界を設計する要素技術です。表示、業務処理、状態の役割を分け、利用側が理解できるpropsとイベントを定め、共通化の範囲と拡張性を判断できるかを評価します。

## Lv0

コンポーネントの責務、公開インターフェース、再利用範囲を説明できず、分割の判断に個別の指示が必要である。

## Lv1

既存の設計例に沿って画面を部品に分け、指定されたpropsとイベントを定義できる。分割理由の整理や粒度の調整には支援が必要である。

## Lv2

責務と変更理由から部品の境界を定め、表示、業務処理、状態の役割を整理できる。利用側が理解できるpropsとイベントを設計し、単独で検証できる構成にできる。

## Lv3

複数画面の差異から共通化範囲を判断し、過剰な汎用化や状態の密結合を避けられる。構成方法、拡張性、変更互換性を比較して設計し、既存部品を段階的に改善できる。

## Lv4

コンポーネントの設計原則、採用・共通化・廃止の基準、カタログ、変更管理を整備できる。複数の利用者による運用を定着させ、重複実装と変更時の影響を減らせる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [React：Reactの流儀（日本語）](https://ja.react.dev/learn/thinking-in-react) — 画面をコンポーネントに分ける手順
- [React：コンポーネントにpropsを渡す（日本語）](https://ja.react.dev/learn/passing-props-to-a-component) — propsの設計
- [React：state構造の選択（日本語）](https://ja.react.dev/learn/choosing-the-state-structure) — 状態の置き場所と形

**代表的なライブラリ・ツール**

- [Storybook](https://storybook.js.org/) — コンポーネントの単独開発とカタログ化
- [Radix Primitives](https://www.radix-ui.com/primitives) — スタイルなしのアクセシブルな部品。shadcn/uiの基盤
- [React Aria](https://react-spectrum.adobe.com/react-aria/) — アクセシブルなUI部品を作るHooks群
- [shadcn/ui](https://ui.shadcn.com/docs) — Radixを基盤にした複製して使うUI部品集

<!-- references:end -->
