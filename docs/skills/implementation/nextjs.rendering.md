---
title: "レンダリングとデータ取得"
description: "Next.jsのServer ComponentsとClient Componentsを使い分け、データ取得とキャッシュを設計する要素技術です。静的・動的レンダリング、ストリーミング、Server Actionsによる更新、再検証、ハイドレーションを理解し、表示の正しさと速度を両立できるかを評価します。"
titleTemplate: ":title | 要素技術 | 習熟度ガイド"
---

# レンダリングとデータ取得

**要素技術ID：** `nextjs.rendering`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** App Routerによる画面構成、REST API連携、非同期処理

<!-- terms:start -->

**前提となる用語：** [Server ComponentsとClient Components](../../guide/glossary.md#server-componentsとclient-components)、[Server Actions](../../guide/glossary.md#server-actions)、[ストリーミング](../../guide/glossary.md#ストリーミング)、[ハイドレーション](../../guide/glossary.md#ハイドレーション)、[キャッシュ](../../guide/glossary.md#キャッシュ)、[キャッシュの再検証](../../guide/glossary.md#キャッシュの再検証)、[API](../../guide/glossary.md#api)

<!-- terms:end -->

Next.jsのServer ComponentsとClient Componentsを使い分け、データ取得とキャッシュを設計する要素技術です。静的・動的レンダリング、ストリーミング、Server Actionsによる更新、再検証、ハイドレーションを理解し、表示の正しさと速度を両立できるかを評価します。

::: start
Next.js公式の「Server and Client Components」で、どちらの部品がどこで動き、何ができて何ができないかを読みます。一覧画面をServer Componentでデータ取得して描画し、並べ替えなど操作が必要な部分だけをClient Componentに切り出せれば、Lv1の入口です。まず読む：[Next.js：Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
:::

## Lv0

サーバー側とブラウザ側のどちらで描画されるかの違い、データ取得の場所、キャッシュの存在を説明できず、データを表示する画面の実装に手順ごとの指示が必要である。

## Lv1

既存例に沿ってServer Componentでデータを取得して表示し、操作が必要な部分をClient Componentに分けられる。キャッシュの設定、再検証、更新処理の実装には支援が必要である。

## Lv2

画面ごとにサーバー側とブラウザ側の境界を決め、fetchのキャッシュと再検証、Server Actionsによる更新、読み込み中の段階的な表示を実装できる。意図しない動的レンダリングやキャッシュの残留、ハイドレーションの不一致を切り分けて修正できる。

## Lv3

静的・動的・ストリーミングの選択、複数層のキャッシュの整合、Server Actionsの競合や部分的な失敗、実行環境（Node.jsとEdge）の制約を踏まえて設計できる。表示速度と鮮度の要件を比較し、既存画面のレンダリング方式を段階的に改善できる。

## Lv4

レンダリング方式とデータ取得の方針、キャッシュと再検証の規約、Server Actionsの共通処理、確認手順を整備できる。チームへの展開と移行を支援し、表示速度、鮮度の不具合、実装工数の改善を実測して方針を更新できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [Next.js：Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) — 境界の決め方と組み合わせ方
- [Next.js：Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data) — サーバー側とブラウザ側のデータ取得、ストリーミング
- [Next.js：use server](https://nextjs.org/docs/app/api-reference/directives/use-server) — Server Actionsの定義と呼び出し、再検証
- [Next.js：Caching](https://nextjs.org/docs/app/deep-dive/caching) — 4層のキャッシュと再検証の仕組み
- [React：Server Components（日本語）](https://ja.react.dev/reference/rsc/server-components) — Server Componentsの考え方

**代表的なライブラリ・ツール**

- [Next.js](https://nextjs.org/docs) — Reactを基にしたフレームワーク
- [TanStack Query](https://tanstack.com/query) — ブラウザ側でのサーバー状態の取得とキャッシュ
- [Zod](https://zod.dev/) — Server Actionsの入力検証

<!-- references:end -->
