---
title: "App Routerによる画面構成"
description: "Next.jsのApp Routerで画面群を構成する要素技術です。ファイル規約によるルーティング、レイアウトの入れ子、動的ルート、ナビゲーション、読み込み中とエラーの表示、メタデータを設計し、URLと画面の対応を保守しやすく実装できるかを評価します。"
titleTemplate: ":title | 要素技術 | 習熟度ガイド"
---

# App Routerによる画面構成

**要素技術ID：** `nextjs.routing`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** React実装、Web基礎

<!-- terms:start -->

**前提となる用語：** [フレームワークとライブラリ](../../guide/glossary.md#フレームワークとライブラリ)、[React](../../guide/glossary.md#react)、[レイアウトとページ](../../guide/glossary.md#レイアウトとページ)、[URL](../../guide/glossary.md#url)、[レンダリング](../../guide/glossary.md#レンダリング)、[SEO](../../guide/glossary.md#seo)

<!-- terms:end -->

Next.jsのApp Routerで画面群を構成する要素技術です。ファイル規約によるルーティング、レイアウトの入れ子、動的ルート、ナビゲーション、読み込み中とエラーの表示、メタデータを設計し、URLと画面の対応を保守しやすく実装できるかを評価します。

::: start
Next.js公式の「Layouts and Pages」で、ディレクトリ構成がそのままURLになる仕組みと、レイアウトが画面をまたいで維持される理由を読みます。一覧と詳細の2画面を、共通レイアウトと動的ルートで作り、リンクで行き来できれば、Lv1の入口です。まず読む：[Next.js：Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
:::

## Lv0

ディレクトリとURLの対応、レイアウトとページの違い、リンクによる画面遷移を説明できず、画面の追加に手順ごとの指示が必要である。

## Lv1

既存の構成に沿ってページとレイアウトを追加し、動的ルートのパラメーターを受け取って表示できる。読み込み中やエラーの表示、メタデータの設定には支援が必要である。

## Lv2

要件が明確な画面群を、共通レイアウト、ルートグループ、動的ルート、読み込み中とエラーの表示を含めて構成できる。ナビゲーション、リダイレクト、メタデータを実装し、URLの設計と画面の対応を自分で検証・修正できる。

## Lv3

並列ルートやインターセプトを含む複雑な画面構成、多言語のルーティング、URLに持たせる状態の設計を判断できる。レイアウトの再描画範囲、ナビゲーション時のデータ再取得、404や権限エラーの扱いを分析し、構成を段階的に改善できる。

## Lv4

画面構成の規約、ディレクトリ構成、メタデータとエラー表示の共通実装、URL設計の基準を整備できる。複数チームへの展開と移行を支援し、画面追加の工数や遷移不具合の改善を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [Next.js：Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages) — ファイル規約、レイアウト、動的ルート、リンク
- [Next.js：Linking and Navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating) — 遷移の仕組みとプリフェッチ
- [Next.js：Error Handling](https://nextjs.org/docs/app/getting-started/error-handling) — エラー表示と404の扱い
- [Next.js：Metadata and OG images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images) — タイトル、説明文、OG画像の設定
- [Next.js：File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions) — layout、page、loading、error などの規約一覧

**代表的なライブラリ・ツール**

- [Next.js](https://nextjs.org/docs) — Reactを基にしたフレームワーク
- [next-intl](https://next-intl.dev/) — App Router向けの多言語対応とルーティング
- [React Router](https://reactrouter.com/) — Next.js以外のReactアプリケーションでのルーティング

<!-- references:end -->
