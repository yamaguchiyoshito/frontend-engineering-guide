---
title: "出典と追加した内容"
description: "チームチェックリストの原典（日本CTO協会 Webフロントエンド版DX Criteria）、そのライセンスと本書で加えた変更、スキル定義の由来、公開方式の公式資料。"
---

# 出典と追加した内容

本書は、一般社団法人日本CTO協会が公開する「Webフロントエンド版DX Criteria」の100項目を原典とするチームチェックリストと、本ガイドで定義した28スキルの習熟度を統合したものです。組織で運用するために、目的、評価手順、判定のルール、改善への接続、記録書式を追加しています。

## チームチェックリストの原典

| 項目 | 内容 |
| :--- | :--- |
| 名称 | Webフロントエンド版DX Criteria（v202402）プロダクトのユーザー体験と変化に適応するチームのためのガイドライン |
| 発行 | 一般社団法人日本CTO協会 |
| URL | [https://dxcriteria.cto-a.org/frontend](https://dxcriteria.cto-a.org/frontend) |
| ライセンス | [クリエイティブ・コモンズ 表示—継承 4.0 国際（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) |
| 本書での利用 | 100項目のチェック項目の原文と、各項目の参照先URLを変更せずに収録 |

[チームチェックリスト](../checklists/index.md)の各項目にある「原文の参照先」は、原典の該当ページです。本書で追加した判定方法や回答例は、原典が定める公式の評価方法ではありません。本書は日本CTO協会の公式な派生物ではなく、同協会の承認や推奨を受けたものでもありません。

### 本書で加えた変更

- 項目No.001〜100の連番、25分野の名称、4つのまとまり（設計・開発、品質、開発・運用、組織・連携）は本書で付けたものです。原典の項目IDや章立てとは異なります。
- 各項目に「望ましい原文への回答（TRUE／FALSE）」と「望ましい回答例」を追加しました。回答例は架空の文面です。
- 原典のアセスメントにある「but」列は使用せず、達成・一部達成・未達・未評価・対象外の判定を追加しました。
- 原典の更新を自動反映する仕組みではありません。原典が改訂された場合は差分を確認し、改訂履歴に記載します。

### 権利とライセンスの扱い

- チェック項目の原文の著作権は、一般社団法人日本CTO協会に帰属します。
- 原典はCC BY-SA 4.0で提供されています。同ライセンスの継承条件に従い、原文を含むチームチェックリストの各ページ、その回答例、単一Markdown中の該当部分は、同じCC BY-SA 4.0で提供します。
- 表示の条件を満たすため、原典の名称、発行者、URL、ライセンスを本ページ、チームチェックリストの各ページ、サイトのフッター、単一Markdownの冒頭に記載しています。
- 原典を再配布・改変する場合は、原典のライセンス条件に従ってください。

## スキル定義の由来

- 28スキル、4領域、スキルID、前提知識、Lv0〜Lv4の定義は本ガイドで作成した内容です。
- 習熟度の判定ルール、評価手順、改善方法、記録書式、記入例も本ガイドで追加した内容です。

## 表記

PRはPull Requestを指します。GitLabを使用する場合は、MR（Merge Request）に読み替えてください。

## 公開方式の公式資料

仕様確認日：2026年9月27日。

- [GitHub Pagesの概要](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Actionsを使ったPages公開](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [VitePress 1系のデプロイ](https://vuejs.github.io/vitepress/v1/guide/deploy)
- [VitePress 1系のサイト内検索](https://vuejs.github.io/vitepress/v1/reference/default-theme-search)

GitHub Freeでも公開リポジトリからGitHub Pagesを公開できます。本実装は公開リポジトリと一般公開サイトの組み合わせを採用し、Enterprise固有機能を使用しません。
