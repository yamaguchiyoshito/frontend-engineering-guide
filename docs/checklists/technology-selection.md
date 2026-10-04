---
title: "技術選定"
description: "Webフロントエンド版DX Criteria 1-5「技術選定」（持続可能な技術スタック）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# 技術選定

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 1. 持続可能な技術スタック  
**小テーマ：** 1-5 技術選定

<!-- terms:start -->

**前提となる用語：** [フレームワークとライブラリ](../guide/glossary.md#フレームワークとライブラリ)、[パッケージと依存関係](../guide/glossary.md#パッケージと依存関係)、[脆弱性](../guide/glossary.md#脆弱性)、[ADR](../guide/glossary.md#adr)  
**関連する要素技術：** [フロントエンド品質保証](../skills/quality/frontend.quality.md)、[Webセキュリティ](../skills/quality/web.security.md)、[TypeScript](../skills/applied-foundation/typescript.basic.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 1-5-1：メトリクスの計測

使用しているライブラリ・サービス・ツールの更新頻度、セキュリティ事象などのメトリクスを追跡し、定期的に（月ごと〜半年ごと）改善を計画・実施している。

::: example
- 利用中のライブラリ・外部サービス・開発ツールを台帳化し、バージョン、更新状況、サポート期限、セキュリティ事象を追跡しています。
- 月次で更新・置き換え・廃止の必要性を確認し、担当者と期限を設定しています。
- 重大な事象は定例を待たずに評価し、対応状況を記録しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/4ad037f798a3490398c62262bef636ba)

## 1-5-2：学習と改善

使用している技術やその周辺技術の情報を収集し、何らかの形で日常的（日ごと〜週ごと）にチーム内共有をしている。

::: example
- 利用技術の公式情報、リリース情報、障害・セキュリティ情報を担当者が確認し、少なくとも週1回、チームの共有場所に要点を投稿しています。
- 自分たちへの影響と必要な対応を併記し、対応が必要な情報はイシューにしています。
- 重要な情報は週次の打ち合わせでも確認しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/565c601ff274406bb53787561ad5470c)

## 1-5-3：プラクティス

技術選定時に数年後のプロダクトビジョンや目標を考慮し、技術的負債の蓄積を避けるための明確な戦略や基準を設け、その遵守を確認している。

::: example
- 数年後に必要となる機能、利用規模、運用体制を踏まえ、保守性・更新可能性・人材確保・費用・移行容易性を技術選定の基準にしています。
- 比較結果と採用理由を設計判断記録に残し、技術責任者が基準への適合を確認しています。
- 許容する技術的負債には理由と解消条件を設定しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/315368610b034a49a8b0ec407edec667)

## 1-5-4：アンチパターン

新しい技術やライブラリについて任意の選定基準に従った調査を行わず、話題になっているなどの動機だけで採用している。

::: example
- 技術の話題性だけを理由に採用していません。
- 解決したい課題、既存技術との差、保守状況、ライセンス、セキュリティ、導入・運用費用、撤退方法を比較しています。
- 必要な検証を小規模に実施し、結果と選定基準に基づいて採否を決定し、その記録を残しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/2d00021c9a904ab38a96a3c1cae55f92)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [ThoughtWorks：Technology Radar](https://www.thoughtworks.com/radar) — 技術の採用段階を整理した公開情報（英語）
- [OpenSSF Scorecard](https://scorecard.dev/) — OSSの保守・セキュリティ状況の評価（英語）

**代表的なツール・サービス**

- [npm trends](https://npmtrends.com/) — パッケージの利用推移の比較
- [Bundlephobia](https://bundlephobia.com/) — パッケージの容量と依存の確認
- [GitHub Advisory Database](https://github.com/advisories) — 脆弱性情報の検索

<!-- references:end -->
