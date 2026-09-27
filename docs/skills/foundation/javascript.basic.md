---
title: "JavaScript"
description: "JavaScriptの構文、関数、オブジェクト、配列を使って処理を実装する要素技術です。要件を関数に分解し、境界値や例外を扱い、スコープや参照が原因の不具合を分析できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# JavaScript

**要素技術ID：** `javascript.basic`  
**領域：** [基礎領域](index.md)  
**評価対象：** 構文、関数、オブジェクト、配列

<!-- terms:start -->

**前提となる用語：** [JavaScript](../../guide/glossary.md#javascript)、[DOM](../../guide/glossary.md#dom)、[Node.js](../../guide/glossary.md#node-js)、[Lintと静的検査](../../guide/glossary.md#lintと静的検査)

<!-- terms:end -->

JavaScriptの構文、関数、オブジェクト、配列を使って処理を実装する要素技術です。要件を関数に分解し、境界値や例外を扱い、スコープや参照が原因の不具合を分析できるかを評価します。

## Lv0

変数、条件分岐、繰り返し、関数の基本を説明できず、短い処理でも手順ごとの指示が必要である。

## Lv1

例を参考に関数や条件分岐を変更し、配列・オブジェクトの値を取得・更新できる。指定された入力に対する結果を確認できる。

## Lv2

要件を関数に分解し、配列・オブジェクトの変換、条件分岐、例外処理を実装できる。空値や境界値を確認し、デバッガーなどで誤りを修正できる。

## Lv3

スコープ、クロージャー、参照共有、暗黙の型変換などが原因の不具合を分析できる。副作用と責務を整理し、複雑な処理を読みやすく検証しやすい構造へ改善できる。

## Lv4

チームで繰り返す処理の設計原則や共通関数、レビュー観点、演習を整備できる。他者への展開を通じて、同種不具合や重複実装の減少を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [MDN：JavaScript](https://developer.mozilla.org/ja/docs/Web/JavaScript) — 言語仕様と組み込みオブジェクトのリファレンス
- [JavaScript Primer](https://jsprimer.net/) — ECMAScript 2015以降を前提にした入門書（日本語、OSS）
- [ECMAScript Language Specification](https://tc39.es/ecma262/) — JavaScriptの言語仕様（英語）

**代表的なライブラリ・ツール**

- [Node.js](https://nodejs.org/ja) — JavaScriptの実行環境
- [ESLint](https://eslint.org/) — JavaScriptの静的検査
- [Prettier](https://prettier.io/) — コード整形
- [Chrome DevTools：JavaScriptのデバッグ](https://developer.chrome.com/docs/devtools/javascript?hl=ja) — ブレークポイントと変数の確認
- [pnpm](https://pnpm.io/ja/) — ディスク効率の高いパッケージ管理

<!-- references:end -->
