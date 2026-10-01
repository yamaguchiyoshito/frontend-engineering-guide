---
title: "コードベース"
description: "Webフロントエンド版DX Criteria 1-1「コードベース」（持続可能な技術スタック）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# コードベース

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 1. 持続可能な技術スタック  
**小テーマ：** 1-1 コードベース

<!-- terms:start -->

**前提となる用語：** [リポジトリ](../guide/glossary.md#リポジトリ)、[TypeScript](../guide/glossary.md#typescript)、[型検査](../guide/glossary.md#型検査)、[Lintと静的検査](../guide/glossary.md#lintと静的検査)、[API](../guide/glossary.md#api)、[OpenAPI](../guide/glossary.md#openapi)  
**関連する要素技術：** [JavaScript](../skills/foundation/javascript.basic.md)、[TypeScript](../skills/applied-foundation/typescript.basic.md)、[REST API連携](../skills/implementation/frontend.api-integration.md)、[チーム開発](../skills/applied-foundation/git.collaboration.md)

<!-- terms:end -->

## 1-1-1：メトリクスの計測

コードのデプロイに対する不具合の発生割合、ライブラリをアップデートする頻度、PRのオープンからクローズまでの時間などを計測し、定期的（月ごと〜半年ごと）に改善のためのアクションを計画・実施している。

::: example
不具合対応を要した本番デプロイの割合、依存ライブラリの更新頻度、PRの作成からクローズまでの時間を、対象期間と集計条件をそろえて月次で確認しています。開発責任者がボトルネックを特定し、担当者・期限を設定した改善イシューを起票しています。翌月に指標の変化と実施結果を振り返っています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/82cc7064d0a94c4485f91b8967b0d6d5)

## 1-1-2：学習と改善

静的型付け言語、コードフォーマッター、リンターを導入している。

::: example
静的型付け言語、フォーマッター、リンターを導入し、設定をリポジトリで管理しています。ローカルとCIで共通のコマンドを使用し、PRごとに型検査・整形確認・静的解析を実行しています。必須の検査に失敗した変更はマージできない設定にしています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/226e30cca75c4469a1a39ad0400bf620)

## 1-1-3：プラクティス

APIレベルで型情報を共有できるツールを利用して、Webアプリと疎通するシステムを含むコードベース全体で型安全性を担保している。

**補足**

例えば、OpenAPI、GraphQL、tRPC、gRPCなどを利用していること。

::: example
API仕様を共通のスキーマで管理し、フロントエンドのAPIクライアント・型定義とバックエンドの入出力定義を生成または照合しています。仕様変更時はCIで互換性と生成物の差分を検証しています。通信境界では実行時にも入力・応答を検証し、コンパイル時の型検査だけでは検出できない不一致を防いでいます。
:::

[原文の参照先](https://dxcriteria.cto-a.org/b9278d2269ee4dccad4e5e638fdcfc92)

## 1-1-4：アンチパターン

静的型付け言語やリンターにおける違反を厳格に運用するあまりコードベースの保守性が低下している。

**補足**

その一方で、静的型付け言語やリンターを利用しているが、any や error を warn に落とすなど、それぞれの違反を勝手に抑制してしまい、曖昧な運用になっていることもアンチパターンと言える。

一時的な違反の抑止措置を講じている場合、その「一時的な違反抑止」が追跡可能になるようにしている場合はその限りではない。要はanyやwarnに変えて抑制するのであれば、なぜそうしたかをちゃんとコードベース内に追跡可能な形で残していることが求められる。

要は厳格すぎても曖昧すぎても問題がある。

::: example
型検査やリンターのルールを満たすためだけの不自然な抽象化や、広範な検査無効化による保守性の低下は生じていません。例外は理由・対象範囲・見直し条件をレビューで確認し、局所的に適用しています。四半期ごとに回避コードや例外設定を棚卸しし、ルールと実装の双方を改善しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/b03cbc7a8d884443a8dc243333d1be03)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [DORA：4つの主要指標](https://dora.dev/guides/dora-metrics-four-keys/) — デプロイ頻度、変更のリードタイム、変更失敗率、復旧時間の定義（英語）
- [typescript-eslint：設定ガイド](https://typescript-eslint.io/getting-started/) — 型付き静的検査の導入と段階的な厳格化

**代表的なツール・サービス**

- [TypeScript](https://www.typescriptlang.org/) — 静的型付け
- [ESLint](https://eslint.org/) — 静的検査
- [Prettier](https://prettier.io/) — コード整形
- [OpenAPI](https://www.openapis.org/)（出典で言及） — APIレベルの型共有
- [GraphQL](https://graphql.org/)（出典で言及） — APIレベルの型共有
- [tRPC](https://trpc.io/)（出典で言及） — TypeScript間の型共有

<!-- references:end -->
