---
title: "アプリケーション設計"
description: "Webフロントエンド版DX Criteria 1-4「アプリケーション設計」（持続可能な技術スタック）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# アプリケーション設計

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 1. 持続可能な技術スタック  
**小テーマ：** 1-4 アプリケーション設計

<!-- terms:start -->

**前提となる用語：** [Webパフォーマンス](../guide/glossary.md#webパフォーマンス)、[Core Web Vitals](../guide/glossary.md#core-web-vitals)、[状態管理](../guide/glossary.md#状態管理)、[レンダリング](../guide/glossary.md#レンダリング)、[レイアウトとページ](../guide/glossary.md#レイアウトとページ)、[Server ComponentsとClient Components](../guide/glossary.md#server-componentsとclient-components)  
**関連する要素技術：** [コンポーネント設計](../skills/implementation/react.component-design.md)、[状態管理](../skills/implementation/react.state-management.md)、[Webパフォーマンス](../skills/quality/web.performance.md)、[App Routerによる画面構成](../skills/implementation/nextjs.routing.md)、[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 1-4-1：メトリクスの計測

アプリケーションの特性に応じてメトリクスの計測を行い、定期的（月ごと〜半年ごと）に改善アクションを計画、実施している。

::: supplement
特に閲覧が多いアプリケーションではレンダリングにかかる時間、インタラクションが多いアプリケーションでは操作中の時間など、アプリケーションの特性に応じてメトリクスの計測を行い、半期程度の頻度でメトリクスに基づいた改善のアクションを計画、実施しているか。
:::

::: example
主要な利用目的に対応する指標を定めています。業務画面では、業務の完了率・所要時間・入力のやり直し率などを計測し、月次で利用部門と確認しています。数値とユーザーの意見から改善対象を選び、担当者・期限・期待効果を設定し、リリース後に結果を評価しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/ab11597c5ac74b0b9a69902633b1e38c)

## 1-4-2：学習と改善

ユーザーの理解と設計学習を両方実施していること。ユーザーに関しては要求の把握やユーザテストの実施、設計に関してはプロトタイプの作成、書籍などのインプット、コードレビューの参画などで学習している。

::: example
機能の設計時に利用者へのヒアリングとユーザーテストを行い、目的・作業手順・困りごとを把握しています。同時に、プロトタイプの比較、設計に関する学習、コードレビューへの参加を通じて実現方法を検討しています。得られた知見と採用した設計の理由を記録し、次の開発に反映しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/709c8abbae5b43449feda5f0617653bf)

## 1-4-3：プラクティス

サービスのユーザー体験を念頭に設計を見直して中長期の開発計画に反映する機会が年次的（半年ごと〜年ごと）にある。

::: example
半年ごとに、利用状況・ユーザーテスト・問い合わせ・障害の情報を基に、ユーザー体験と設計を見直しています。個別画面の修正では解決できない課題も整理し、構造変更や基盤改善を中長期の開発計画に反映しています。優先順位、想定効果、実施時期、責任者を明確にしています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/23b6a510ebdf4123b9d1d57c7dcd4ff2)

## 1-4-4：アンチパターン

組織内での共通化を優先するばかりに、サービス特性に合わない設計を転用してしまいユーザー体験を損ねている。

::: example
共通設計の適用時は、利用者の作業手順やサービス固有の要件への適合を確認しており、共通化を理由にユーザー体験を損なう設計を採用していません。適合しない場合は、共通部分と個別対応する部分を分けて設計しています。判断理由とユーザーテストの結果を記録しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/9d347242ba9f4270be7a4747e9c4f168)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [web.dev：Core Web Vitals](https://web.dev/articles/vitals?hl=ja) — 閲覧・操作の特性に応じた指標
- [web.dev：Interaction to Next Paint](https://web.dev/articles/inp?hl=ja) — 操作中の応答性の指標
- [デジタル庁：デザインシステム](https://design.digital.go.jp/) — ユーザー理解に基づく設計指針の公開例

**代表的なツール・サービス**

- [Lighthouse](https://developer.chrome.com/docs/lighthouse?hl=ja) — 特性に応じた計測
- [web-vitals](https://github.com/GoogleChrome/web-vitals) — 実利用データの計測

<!-- references:end -->
