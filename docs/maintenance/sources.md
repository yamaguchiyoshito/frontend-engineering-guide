---
title: "出典と追加した内容"
description: "チームチェックリストの出典（日本CTO協会 Webフロントエンド版DX Criteria）、そのライセンスと本書で加えた変更、要素技術の由来、公開方式の公式資料。"
---

# 出典と追加した内容

本書は、一般社団法人日本CTO協会が公開する「Webフロントエンド版DX Criteria」の100項目を出典とするチームチェックリストと、本ガイドで定義した28の要素技術の習熟度を統合したものです。組織で運用するために、目的、評価手順、判定のルール、改善への接続、記録書式を追加しています。

## チームチェックリストの出典

| 項目 | 内容 |
| :--- | :--- |
| 名称 | Webフロントエンド版DX Criteria（v202402）プロダクトのユーザー体験と変化に適応するチームのためのガイドライン |
| 発行 | 一般社団法人日本CTO協会 |
| URL | [https://dxcriteria.cto-a.org/frontend](https://dxcriteria.cto-a.org/frontend) |
| ライセンス | [クリエイティブ・コモンズ 表示—継承 4.0 国際（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) |
| 本書での利用 | 5つの大テーマ、25の小テーマ、4つの観点の分類と名称、100項目の原文と補足説明、各項目の参照先URLを変更せずに収録 |

[チームチェックリスト](../checklists/index.md)の各項目にある「原文の参照先」は、出典の該当ページです。出典の説明は[概要](https://dxcriteria.cto-a.org/e29172142f0f4eacbc17f3d94c8160d0)、[ポリシーと構造](https://dxcriteria.cto-a.org/90a7445d540148408343e83f4cbbecac)、[使い方](https://dxcriteria.cto-a.org/db7e371398c2464792dc25d79e573ba1)を参照してください。本書で追加した判定方法や回答例は、出典が定める公式の評価方法ではありません。本書は日本CTO協会の公式な派生物ではなく、同協会の承認や推奨を受けたものでもありません。

### 本書で加えた変更

- 分類と名称は出典の5つの大テーマ（持続可能な技術スタック、ユーザー体験を支える品質、安定的なデリバリー、効果的なシステム設計、成長できるチーム）、大テーマごとの5つの小テーマ、小テーマごとの4つの観点（メトリクスの計測、学習と改善、プラクティス、アンチパターン）に従います。各ページと項目は出典のID（例：2-3、2-3-1）と観点名で示しています。
- 各項目の文面と補足説明は、出典のとおり収録しています。
- 各項目に「望ましい回答例」を追加しました。回答例は架空の文面です。
- 改善の管理用に、達成・一部達成・未達・未評価・対象外の判定と記録書式を追加しました。出典のアセスメント方法とは別のものです。
- 出典の更新を自動反映する仕組みではありません。出典が改訂された場合は差分を確認し、改訂履歴に記載します。

### 権利とライセンスの扱い

- チェック項目の原文の著作権は、一般社団法人日本CTO協会に帰属します。
- 出典はCC BY-SA 4.0で提供されています。同ライセンスの継承条件に従い、本ガイド全体（要素技術、使い方、チェックリスト、回答例、記録書式、記入例、スクリプト、サイト設定）を同じ[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ja)で提供します。全文はリポジトリの `LICENSE` にあります。
- 表示の条件を満たすため、出典の名称、発行者、URL、ライセンスを本ページ、チームチェックリストの各ページ、サイトのフッター、単一Markdownの冒頭に記載しています。
- 本ガイドを利用・再配布・改変する場合は、本ガイドと出典の名称、URL、ライセンスを表示し、派生物もCC BY-SA 4.0で提供してください。

## 要素技術の由来

- 28の要素技術、4領域、要素技術ID、前提知識、Lv0〜Lv4の定義は本ガイドで作成した内容です。
- 習熟度の判定ルール、評価手順、改善方法、記録書式、記入例も本ガイドで追加した内容です。これらもCC BY-SA 4.0で提供します。

## 表記

PRはPull Requestを指します。GitLabを使用する場合は、MR（Merge Request）に読み替えてください。

## 公開方式の公式資料

仕様確認日：2026年9月27日。

- [GitHub Pagesの概要](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Actionsを使ったPages公開](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [VitePress 1系のデプロイ](https://vuejs.github.io/vitepress/v1/guide/deploy)
- [VitePress 1系のサイト内検索](https://vuejs.github.io/vitepress/v1/reference/default-theme-search)

GitHub Freeでも公開リポジトリからGitHub Pagesを公開できます。本実装は公開リポジトリと一般公開サイトの組み合わせを採用し、Enterprise固有機能を使用しません。
