---
title: "非同期処理"
description: "PromiseやasyncとawaitによるJavaScriptの非同期処理を実装する要素技術です。読み込み中、成功、失敗の状態と処理の順序を扱い、競合、キャンセル、再試行を含む処理を設計できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# 非同期処理

**要素技術ID：** `javascript.async`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** JavaScript

<!-- terms:start -->

**前提となる用語：** [非同期処理](../../guide/glossary.md#非同期処理)、[Promise](../../guide/glossary.md#promise)、[HTTP](../../guide/glossary.md#http)、[API](../../guide/glossary.md#api)

<!-- terms:end -->

PromiseやasyncとawaitによるJavaScriptの非同期処理を実装する要素技術です。読み込み中、成功、失敗の状態と処理の順序を扱い、競合、キャンセル、再試行を含む処理を設計できるかを評価します。

## Lv0

同期・非同期の違い、Promiseやawaitの役割を説明できず、処理順序や失敗時の動作を追うことに支援が必要である。

## Lv1

例に沿ってasync/awaitで処理を待ち、成功・失敗時の処理を記述できる。支援を受けて実行順序を確認できる。

## Lv2

逐次処理と並列処理を使い分け、読み込み中・成功・失敗を扱える。処理の完了順序を確認し、例外の取りこぼしや二重実行を防ぐ実装と検証ができる。

## Lv3

応答順序の逆転、キャンセル、タイムアウト、再試行が絡む処理を設計できる。競合や古い応答による上書きを再現・修正し、再試行時の副作用も評価できる。

## Lv4

非同期処理の共通方針と再利用部品、競合・遅延・失敗の検証方法を整備できる。他者の利用結果を基に、非同期処理に起因する不具合と調査工数を改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [MDN：非同期JavaScript](https://developer.mozilla.org/ja/docs/Learn_web_development/Extensions/Async_JS) — Promise、async/awaitの入門
- [MDN：Promise](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise) — Promiseのリファレンス
- [MDN：AbortController](https://developer.mozilla.org/ja/docs/Web/API/AbortController) — 非同期処理のキャンセル
- [JavaScript Primer：非同期処理](https://jsprimer.net/basic/async/) — コールバック、Promise、async/awaitの解説（日本語）

**代表的なライブラリ・ツール**

- [typescript-eslint：no-floating-promises](https://typescript-eslint.io/rules/no-floating-promises/) — 未処理のPromiseの検出
- [eslint-plugin-promise](https://github.com/eslint-community/eslint-plugin-promise) — Promiseの誤用の検出

<!-- references:end -->
