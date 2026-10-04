---
title: "サーバー"
description: "Webフロントエンド版DX Criteria 4-1「サーバー」（効果的なシステム設計）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# サーバー

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 4. 効果的なシステム設計  
**小テーマ：** 4-1 サーバー

<!-- terms:start -->

**前提となる用語：** [フロントエンドとバックエンド](../guide/glossary.md#フロントエンドとバックエンド)、[API](../guide/glossary.md#api)、[REST API](../guide/glossary.md#rest-api)、[OpenAPI](../guide/glossary.md#openapi)、[JSON](../guide/glossary.md#json)、[モック](../guide/glossary.md#モック)、[Node.js](../guide/glossary.md#node-js)  
**関連する要素技術：** [REST API連携](../skills/implementation/frontend.api-integration.md)、[Web基礎](../skills/foundation/web.basic.md)、[React実装](../skills/implementation/react.basic.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 4-1-1：メトリクスの計測

サーバーアプリケーションのリソースについてメトリクスを収集している。

**補足**

リソースのメトリクスには例として下記のものが挙げられる。

- CPU利用率
- メモリ利用率
- ディスク使用量
- ネットワーク帯域幅

::: example
サーバーアプリケーションのCPU、メモリ、ディスク、接続数、キュー滞留など、採用構成に応じたリソース指標を継続的に収集しています。応答時間、エラー、リクエスト量と併せて確認でき、負荷増加やリソース枯渇を検知できます。ダッシュボードと履歴を開発・運用の関係者で共有しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/e6cd3e59c75643768c338931e021c64b)

## 4-1-2：学習と改善

Webフロントエンド開発者がサーバーの実装や運用に関わる場合、バックエンドやインフラ領域の学習機会を提供している。

::: example
フロントエンド開発者がサーバーの実装・運用を担当する前に、API、データストア、認証・認可、デプロイ、監視の学習機会を設けています。検証環境での演習とバックエンド・インフラ担当者との共同作業を行っています。担当範囲に必要な知識を確認し、習得状況に応じて支援者を配置しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/4ef3b8baf04a494f9b0fd9c43026b803)

## 4-1-3：プラクティス

API実装が分業下にある場合、そのインターフェースをWebフロントエンドの実装者が主導して定義している。

**補足**

Webフロントエンド開発者がAPIのインタフェースを先行して決定し、バックエンドに対して要求を出す Consumer Driven Contracting な開発スタイルを実践している。バックエンドの API を待ってから開発をすることで、フロントエンドの開発開始が遅れてしまうことがない。

::: example
フロントエンド実装者が画面と利用者の操作から必要なデータ・操作・応答を整理し、APIインターフェースの原案作成を主導しています。バックエンド担当者と認可、整合性、性能、実装制約を確認して合意しています。合意した仕様を共通管理し、両者が仕様に基づいて実装・検証しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/2fa6de80616744f397bff855ff6e8eec)

## 4-1-4：アンチパターン

Webフロントエンドとバックエンドの分業している場合、画面の生成やデータの処理方法等の実現手段について片方による一方的な意思決定が行われている。

::: example
画面の生成場所、データ取得・加工、状態管理、エラー処理などの実現方法を、フロントエンドとバックエンドの担当者が共同で検討しています。ユーザー体験、性能、セキュリティ、運用負担を比較し、責任分界と判断理由を記録しています。一方の都合だけで他方の実装を制約する決定は行っていません。
:::

[原文の参照先](https://dxcriteria.cto-a.org/ea1cc6fba8d24bc79590f66fc4a55d73)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [Martin Fowler：Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html)（出典で言及） — 利用側主導のAPI定義（英語）
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — APIインターフェースの記述形式（英語）
- [Node.js：ドキュメント](https://nodejs.org/ja/docs) — サーバー実装の学習資料

**代表的なツール・サービス**

- [Pact](https://pact.io/) — 契約テスト
- [Mock Service Worker](https://mswjs.io/) — APIモック
- [OpenTelemetry](https://opentelemetry.io/ja/docs/) — リソース指標の収集の標準

<!-- references:end -->
