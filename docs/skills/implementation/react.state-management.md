---
title: "状態管理"
description: "画面の状態をどこに置き、どう更新するかを設計する要素技術です。ローカル、共有、URL、サーバー由来の状態を区別し、同期、キャッシュ、楽観的更新、部分的な失敗を含む遷移を扱えるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# 状態管理

**要素技術ID：** `react.state-management`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** React、非同期処理

<!-- terms:start -->

**前提となる用語：** [React](../../guide/glossary.md#react)、[propsと状態](../../guide/glossary.md#propsと状態)、[状態管理](../../guide/glossary.md#状態管理)、[非同期処理](../../guide/glossary.md#非同期処理)、[キャッシュ](../../guide/glossary.md#キャッシュ)、[楽観的更新](../../guide/glossary.md#楽観的更新)

<!-- terms:end -->

画面の状態をどこに置き、どう更新するかを設計する要素技術です。ローカル、共有、URL、サーバー由来の状態を区別し、同期、キャッシュ、楽観的更新、部分的な失敗を含む遷移を扱えるかを評価します。

## Lv0

状態と計算で求められる値の違い、状態の持ち主を説明できず、状態の追加・更新に手順ごとの指示が必要である。

## Lv1

既存例に沿ってローカル状態を追加し、指定された操作で更新できる。親子間での受け渡しや複数状態の調整には支援が必要である。

## Lv2

ローカル状態、共有状態、URLに持たせる状態、サーバー由来の状態を区別し、配置先を選べる。標準的な画面で更新・初期化・取得失敗を扱い、状態の重複を避けられる。

## Lv3

複数画面の同期、キャッシュ、楽観的更新、競合、部分的な失敗を含む状態遷移を設計できる。不整合を再現し、状態の所有者と更新経路を整理して改善できる。

## Lv4

状態の分類・配置・同期・破棄に関する方針と共通実装を整備できる。チームへの移行・教育を支援し、状態不整合や変更工数の改善を実測して方針を更新できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [React：stateの管理（日本語）](https://ja.react.dev/learn/managing-state) — 状態の設計とリフトアップ
- [React：useReducer（日本語）](https://ja.react.dev/reference/react/useReducer) — 複雑な更新ロジックの整理
- [TanStack Query：概要](https://tanstack.com/query/latest/docs/framework/react/overview) — サーバー状態の考え方

**代表的なライブラリ・ツール**

- [TanStack Query](https://tanstack.com/query) — サーバー状態の取得、キャッシュ、更新
- [Zustand](https://zustand.docs.pmnd.rs/) — 軽量な共有状態管理
- [Jotai](https://jotai.org/) — 原子単位の状態管理
- [Redux Toolkit](https://redux-toolkit.js.org/) — Reduxの標準ツールセット

<!-- references:end -->
