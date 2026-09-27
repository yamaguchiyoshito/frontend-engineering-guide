---
title: "デプロイ"
description: "Webフロントエンド版DX Criteria 3-3「デプロイ」（安定的なデリバリー）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 開発ガイド"
---

# デプロイ

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 3. 安定的なデリバリー  
**小テーマ：** 3-3 デプロイ

## 3-3-1：メトリクスの計測

デプロイの頻度や変更のリードタイムなどデプロイ指標の計測結果がチーム全体に共有されていて、チームで定期的（月ごと〜半年ごと）に振り返っている。

::: example
本番デプロイの頻度、変更のリードタイム、失敗や切り戻しの発生状況を継続的に記録しています。リードタイムの起点と終点を定義し、チーム全員が同じ指標を参照できます。月次で待ち時間やリスクを振り返り、改善施策と担当者を決め、翌月に効果を確認しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/5505e01965bd4a7988768990400a9ef1)

## 3-3-2：学習と改善

新しいバージョンをリリースしたあと、システムの安定性やユーザー体験に関わるメトリクスの変化などを検知でき、改善や切り戻しの意思決定が行えるようになっている。

::: example
リリース前後のエラー率、応答時間、主要操作の成功率をバージョン単位で比較できます。リリース前に監視期間、許容する変化、切り戻し基準、判断者を決めています。基準を超えた場合は影響を調査し、追加修正・機能停止・切り戻しを判断して、結果を記録しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/20f4be4927284d089f16e74e0cc07ce1)

## 3-3-3：プラクティス

段階的に新しいバージョンを提供したり（Canary Release）、機能の ON/OF を安全に切り替えたり（Feature Toggle）できる仕組みを導入している。

::: example
利用者や環境を限定した段階的な提供と、機能フラグによる有効・無効の切り替えを実施できる仕組みを導入しています。切り替え権限と操作履歴を管理し、停止時の画面動作やデータへの影響を事前に検証しています。機能フラグには管理者と撤去条件を定めています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/82ab02086c5844339849a97e17488872)

## 3-3-4：アンチパターン

デプロイするたびにサービスが何らか不安定になるため、デプロイ頻度が抑制されてしまっている。

**補足**

Webアプリケーションが依存する外部サービスにおいてリリース時の整合性が保証されていない、リリース前に開かれていた場合に古いファイルへのアクセスが発生して404が生じるなどリリース前後の潜在的な不具合が見過ごされているケースを指す。

影響が僅少であれば状況に応じてリスクに目を瞑る選択肢もあるが、リリース頻度に影響を与えるようなネガティブがあれば改善すべきである。

::: example
デプロイに伴う不安定化を理由に、必要なリリースを先延ばしする状態にはなっていません。自動テスト、段階的な提供、リリース後の監視、切り戻し手順を整備し、変更を小さく分けて適用しています。デプロイ失敗は原因と対策を記録し、同じ原因が繰り返されないよう改善しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/b0f3daace7344be38a587da37543f600)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [DORA：4つの主要指標](https://dora.dev/guides/dora-metrics-four-keys/) — デプロイ頻度とリードタイム（英語）
- [Google SRE Workbook：Canarying Releases](https://sre.google/workbook/canarying-releases/)（出典で言及） — 段階的リリースの考え方（英語）
- [Martin Fowler：Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)（出典で言及） — 機能の切り替えの設計（英語）

**代表的なツール・サービス**

- [OpenFeature](https://openfeature.dev/) — Feature Toggleの標準API
- [GitHub Actions：環境](https://docs.github.com/ja/actions/deployment/targeting-different-environments/using-environments-for-deployment) — デプロイ先ごとの保護と承認

**関連する要素技術**

- [チーム開発](../skills/applied-foundation/git.collaboration.md)、[フロントエンド品質保証](../skills/quality/frontend.quality.md)、[E2Eテスト](../skills/quality/test.e2e.md)

<!-- references:end -->
