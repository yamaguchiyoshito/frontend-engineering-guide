---
title: "CI/CD"
description: "Webフロントエンド版DX Criteria 3-5「CI/CD」（安定的なデリバリー）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# CI/CD

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 3. 安定的なデリバリー  
**小テーマ：** 3-5 CI/CD

<!-- terms:start -->

**前提となる用語：** [CI](../guide/glossary.md#ci)、[デプロイとCD](../guide/glossary.md#デプロイとcd)、[Pull RequestとMerge Request](../guide/glossary.md#pull-requestとmerge-request)、[Lintと静的検査](../guide/glossary.md#lintと静的検査)、[単体テスト](../guide/glossary.md#単体テスト)、[環境](../guide/glossary.md#環境)  
**関連する要素技術：** [チーム開発](../skills/applied-foundation/git.collaboration.md)、[フロントエンド品質保証](../skills/quality/frontend.quality.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 3-5-1：メトリクスの計測

CI/CDを取り扱う関係者で運用を振り返る機会が定期的（月ごと〜半年ごと）にあり、継続的な改善を行っている。

::: example
開発・テスト・運用の関係者が月次でCI/CDの運用を振り返っています。成功率、待機時間、実行時間、失敗原因、運用負担を確認し、改善項目に優先順位と担当者を設定しています。パイプライン変更後の結果を次回の振り返りで確認し、改善履歴を残しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/94598a6d449e46628ed571dbf648aad2)

## 3-5-2：学習と改善

CI/CDの各種設定ファイル以外にパイプラインの全体像が分かるドキュメントなどのナレッジがありチーム内で更新、共有ができている。

::: example
CI/CDの起動条件、ジョブの流れ、依存関係、成果物、環境、承認箇所、失敗時の対応を文書と構成図で共有しています。設定変更と同じPRで関連文書を更新しています。新規参加者が実行状況を確認し、失敗原因を調査して再実行できる手順を整備しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/e1e0b35148074237a1f51a6905031db6)

## 3-5-3：プラクティス

CI/CDのパイプライン全体が自動化されている。

::: example
変更の取り込みから静的検査、テスト、ビルド、成果物保管、デプロイ、稼働確認までをパイプラインで自動実行しています。手作業によるファイル転送や本番サーバー上のコマンド実行を必要としません。承認が必要な環境では承認ゲートを明示し、承認後の実行と結果記録を自動化しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/5bbd4786456447f58a7502539339098f)

## 3-5-4：アンチパターン

CI/CDのパイプラインを開発チームの当事者が自分たちで管理、改善できていない。

::: supplement
専任の運用チームの関与を否定するのものでは決してないが、Webフロントエンド領域の担当者が自発的に改善アクションを起こさない、起こせない等の状況は健全ではない。

Webフロントエンド技術の知見を活かすことでCI/CDパイプラインひいてはデリバリーの改善に寄与できるはずである。
:::

::: example
開発チーム自身がCI/CD設定を理解し、PRを通じて変更・検証・改善できる権限と手順を持っています。共通基盤を管理するチームとの責任分界と相談先も明確にしています。担当者を複数名置き、設定変更や障害調査が外部の特定担当者だけに依存する状態にはなっていません。
:::

[原文の参照先](https://dxcriteria.cto-a.org/83dbabd5a8bb43a78b2e1ef4ebced61d)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [GitHub Docs：GitHub Actions](https://docs.github.com/ja/actions) — パイプラインの構成と運用
- [DORA：継続的デリバリー](https://dora.dev/capabilities/continuous-delivery/) — CI/CDの能力の解説（英語）
- [GitLab Docs：CI/CD](https://docs.gitlab.com/ci/) — GitLabでのパイプラインの構成と運用

**代表的なツール・サービス**

- [GitHub Actions](https://docs.github.com/ja/actions) — パイプラインの自動化
- [actionlint](https://github.com/rhysd/actionlint) — ワークフロー定義の静的検査
- [act](https://github.com/nektos/act) — ワークフローのローカル実行
- [GitLab CI/CD](https://docs.gitlab.com/ci/) — GitLabでのパイプラインの自動化

<!-- references:end -->
