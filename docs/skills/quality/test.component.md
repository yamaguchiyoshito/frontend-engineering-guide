---
title: "コンポーネントテスト"
description: "コンポーネントの表示と操作をテストする要素技術です。利用者が認識する状態、入力、イベント、エラーを基準に検証し、非同期の更新やフォーカスを扱い、不安定なテストを分析して改善できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# コンポーネントテスト

**要素技術ID：** `test.component`  
**領域：** [品質・高度化領域](index.md)  
**主な前提：** React

<!-- terms:start -->

**前提となる用語：** [コンポーネントテスト](../../guide/glossary.md#コンポーネントテスト)、[コンポーネント](../../guide/glossary.md#コンポーネント)、[モック](../../guide/glossary.md#モック)、[アクセシビリティ](../../guide/glossary.md#アクセシビリティ)

<!-- terms:end -->

コンポーネントの表示と操作をテストする要素技術です。利用者が認識する状態、入力、イベント、エラーを基準に検証し、非同期の更新やフォーカスを扱い、不安定なテストを分析して改善できるかを評価します。

::: start
React Testing Libraryの入門で、利用者の見え方で要素を取得する考え方を読みます。ボタンを押すと表示が変わる部品について、操作と結果の確認をテストとして書ければ、Lv1の入口です。まず読む：[React Testing Library：入門](https://testing-library.com/docs/react-testing-library/intro/)
:::

## Lv0

コンポーネントの表示と利用者の操作を何で検証するか説明できず、既存テストの実行や変更に支援が必要である。

## Lv1

既存例に沿って部品を描画し、文字の表示やクリック後の変化を確認するテストを追加できる。必要なモックやプロバイダーは支援を受けて設定できる。

## Lv2

利用者が認識する表示・操作を基準に、主要状態、入力、イベント、エラーを検証できる。非同期の表示更新を待ち、内部実装に依存しすぎない要素の特定と期待結果を記述できる。

## Lv3

複雑な相互作用、フォーカス、外部状態、非同期競合を検証できる。テストの不安定さや過度なモックを分析し、部品の契約を守りながら検証構成を改善できる。

## Lv4

共通UIの検証パターン、テスト環境、補助処理、CI運用を整備できる。複数の開発者に展開し、UI不具合の流出、テストの不安定さ、保守工数を改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [React Testing Library：入門](https://testing-library.com/docs/react-testing-library/intro/) — Reactコンポーネントの検証方法
- [Testing Library：クエリの優先順位](https://testing-library.com/docs/queries/about/#priority) — 要素の特定方法の選び方
- [Vitest：ブラウザモード](https://vitest.dev/guide/browser/) — 実ブラウザでのコンポーネントテスト

**代表的なライブラリ・ツール**

- [Testing Library](https://testing-library.com/) — 利用者視点の要素特定と操作
- [user-event](https://testing-library.com/docs/user-event/intro) — 実際の操作に近いイベント発火
- [Storybook インタラクションテスト](https://storybook.js.org/docs/writing-tests/interaction-testing) — Story上での検証
- [vitest-axe](https://github.com/chaance/vitest-axe) — Vitestでのアクセシビリティ自動検証

<!-- references:end -->
