---
title: "インフラ"
description: "Webフロントエンド版DX Criteria 4-2「インフラ」（効果的なシステム設計）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# インフラ

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 4. 効果的なシステム設計  
**小テーマ：** 4-2 インフラ

<!-- terms:start -->

**前提となる用語：** [サーバー](../guide/glossary.md#サーバー)、[CDN](../guide/glossary.md#cdn)、[環境](../guide/glossary.md#環境)、[Infrastructure as Code](../guide/glossary.md#infrastructure-as-code)、[SLO](../guide/glossary.md#slo)  
**関連する要素技術：** [Web基礎](../skills/foundation/web.basic.md)、[Webパフォーマンス](../skills/quality/web.performance.md)

<!-- terms:end -->

## 4-2-1：メトリクスの計測

インフラおよびシステムの可用性についてメトリクスを収集している。

**補足**

可用性のメトリクスに関しては例として下記のものが挙げられる。

- レスポンス時間
- エラー発生率
- ダウンタイム
- MTTR

::: example
インフラとシステムの稼働状況、外形監視の成功率、主要機能の利用可否、障害時間を継続的に収集しています。可用性の集計対象・時間帯・除外条件を定義し、コンポーネント単位とサービス全体で確認できます。目標との差と停止原因を月次で振り返り、改善に反映しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/5dc08086fa834135a2f0f6cfadcc0751)

## 4-2-2：学習と改善

自分たちの設計を実施する上での最適な方法を模索するため、Webフロントエンド開発者がインフラ設計に参画している。

::: example
フロントエンド開発者がインフラ設計の検討に参加し、画面配信、キャッシュ、認証、描画方式、性能、リリース方法に関する要件を提示しています。インフラ担当者と代替構成を比較し、費用・運用・ユーザー体験を踏まえて設計を決めています。検証結果と採用理由を共同で記録しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/61a192f91ec741ceb3f4edb05b6d6dd5)

## 4-2-3：プラクティス

開発者のスキルセットに応じて必要があればインフラやシステムの一部としてPlatform as a Serviceを利用できる。

**補足**

Platform as a Service の具体例として下記のものが挙げられる。

- Vercel
- Firebase
- Supabase
- Amplify

::: example
チームのスキルと運用負荷に応じてPaaSを選択できる評価・承認の手順があります。要件への適合、セキュリティ、可用性、費用、データの扱い、移行可能性を確認し、必要に応じて試用しています。採用可能な条件と申請先を共有し、運用要員の制約も踏まえて選択できます。
:::

[原文の参照先](https://dxcriteria.cto-a.org/4e55f2c1c6f347e184f33e4b65a05519)

## 4-2-4：アンチパターン

既定のインフラ構成が固まってしまっていて、新規開発やリプレース時などにインフラの再設計を検討する余地がない。

::: example
新規開発やリプレース時には既存構成の前提を再確認し、要件・規模・運用体制に応じたインフラの再設計を検討しています。標準構成から変更するための判断基準と手順を設けています。変更の効果、費用、移行リスクを比較し、継続または変更の理由を記録しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/3babe5df95bb423aaeb05a6e384a797d)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [Google SRE Book：Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — 可用性指標の考え方（英語）
- [AWS Well-Architected Framework](https://aws.amazon.com/jp/architecture/well-architected/) — インフラ設計の観点

**代表的なツール・サービス**

- [Vercel](https://vercel.com/)（出典で言及） — Platform as a Service
- [Firebase](https://firebase.google.com/?hl=ja)（出典で言及） — Platform as a Service
- [Supabase](https://supabase.com/)（出典で言及） — Platform as a Service
- [AWS Amplify](https://aws.amazon.com/jp/amplify/)（出典で言及） — Platform as a Service

<!-- references:end -->
