---
title: "E2Eテスト"
description: "利用者の業務シナリオをブラウザ操作で検証する要素技術です。開始状態、操作、期待結果、後始末を実装してCIで実行し、複数ロールや外部連携を含むシナリオの安定性と速度を改善できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# E2Eテスト

**要素技術ID：** `test.e2e`  
**領域：** [品質・高度化領域](index.md)  
**主な前提：** フォーム、API連携

<!-- terms:start -->

**前提となる用語：** [E2Eテスト](../../guide/glossary.md#e2eテスト)、[CI](../../guide/glossary.md#ci)、[不安定なテスト](../../guide/glossary.md#不安定なテスト)、[環境](../../guide/glossary.md#環境)

<!-- terms:end -->

利用者の業務シナリオをブラウザ操作で検証する要素技術です。開始状態、操作、期待結果、後始末を実装してCIで実行し、複数ロールや外部連携を含むシナリオの安定性と速度を改善できるかを評価します。

## Lv0

利用者の業務シナリオとE2Eの検証範囲を説明できず、実行環境の準備や既存シナリオの確認に支援が必要である。

## Lv1

用意された手順とデータを使ってブラウザ操作を自動化し、指定された画面表示と完了結果を確認できる。失敗の調査は支援を受けて行える。

## Lv2

主要な業務シナリオについて、開始状態、操作、期待結果、後始末を実装できる。安定した要素の特定と待機方法を選び、CIで実行し、失敗時の証跡を確認できる。

## Lv3

複数ロール、画面横断、非同期反映、外部連携を含むシナリオを設計できる。アプリ、テスト、データ、環境の問題を切り分け、並列実行やデータ分離で安定性と速度を改善できる。

## Lv4

業務リスクに基づくE2E対象の選定、共通シナリオ、データ・環境管理、CI結果の分析と保守体制を整備できる。チームで運用し、実行時間、不安定な失敗、重大不具合の検出状況を改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [Playwright：ドキュメント](https://playwright.dev/docs/intro) — 導入からCI実行までの公式ガイド
- [Playwright：ベストプラクティス](https://playwright.dev/docs/best-practices) — 安定した要素特定と待機の指針
- [Cypress：ドキュメント](https://docs.cypress.io/) — 代替のE2Eテストツール
- [Playwright：テストのシャーディング](https://playwright.dev/docs/test-sharding) — CIでの並列分割実行
- [Playwright：スクリーンショット比較](https://playwright.dev/docs/test-snapshots) — toHaveScreenshotによる視覚差分の検証

**代表的なライブラリ・ツール**

- [Playwright](https://playwright.dev/) — 複数ブラウザ対応のE2Eテスト
- [Cypress](https://www.cypress.io/) — ブラウザ内で動くE2Eテスト
- [GitHub Actions](https://docs.github.com/ja/actions) — CIでの実行と証跡の保存
- [MagicPod](https://magicpod.com/) — ノーコードのE2Eテスト自動化（商用）
- [GitLab CI/CD](https://docs.gitlab.com/ci/) — GitLabでのパイプライン実行

<!-- references:end -->
