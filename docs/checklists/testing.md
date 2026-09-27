---
title: "テスト"
description: "Webフロントエンド版DX Criteria 3-1「テスト」（安定的なデリバリー）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 開発ガイド"
---

# テスト

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 3. 安定的なデリバリー  
**小テーマ：** 3-1 テスト

## 3-1-1：メトリクスの計測

CIにおける各種テストの所要時間が常に記録されていて必要なときに参照できる状態にある。

::: example
CIで実行する各テストジョブと、取得可能なテストケース単位の所要時間を毎回記録しています。実行対象、コミット、成功・失敗、再実行の情報と関連付けて保存し、チームが履歴を参照できます。実行時間の推移と遅いテストを確認できる状態にしています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/190cdc10d51f4d568b2b0cf873c3051d)

## 3-1-2：学習と改善

テストのメンテナンス工数が確保されていて、頻繁に失敗するなど効率性や頑健性を妨げるテストが放置されない仕組みができている。

::: example
スプリント計画にテスト保守の工数を含め、不安定なテスト、実行時間の増加、重複、陳腐化を週次で確認しています。問題には担当者と修正期限を設定しています。一時的にテストを隔離する場合も、代替の確認方法と復帰期限を定め、無効化したまま放置しない運用にしています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/87297b959d8542b4a973916344583413)

## 3-1-3：プラクティス

開発者向けの方針として、品質管理のために何をテストし、どのようなテスト手法を用いるかが明確に文書化されている。

::: example
品質リスクに応じて何をどの層で検証するかを、テスト方針として文書化しています。単体・コンポーネント・API・結合・E2E・非機能の対象、実行時点、担当、期待結果の根拠を明記しています。自動化と手動確認の分担、テストデータ、合否基準、変更時の見直し方法も共有しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/931331054af045db9bb8a1279fa5e275)

## 3-1-4：アンチパターン

テスト工程が計画的に整備されていないことによる不具合の顕在化で開発効率やユーザー体験の低下が起きている。

::: example
開発計画の段階でテスト対象・観点・環境・データ・担当・実施時期を確定し、実装と並行して準備しています。変更箇所と業務上のリスクから回帰テストを選定し、リリース前に結果を確認しています。テスト工程の未整備による同種不具合の流出を繰り返さないよう、発生原因を方針とケースへ反映しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/5a32cc51bb894f3da6a2998366a838ff)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [Martin Fowler：The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — テスト層の配分と方針の文書化（英語）
- [Playwright：ベストプラクティス](https://playwright.dev/docs/best-practices) — 不安定なテストを減らす指針
- [Testing Library：指針](https://testing-library.com/docs/guiding-principles) — 頑健なテストの考え方（英語）
- [Martin Fowler：UnitTest](https://martinfowler.com/bliki/UnitTest.html) — SociableテストとSolitaryテストの区別（英語）
- [Playwright：テストのシャーディング](https://playwright.dev/docs/test-sharding) — CIでの並列分割実行

**代表的なツール・サービス**

- [Vitest](https://vitest.dev/) — 単体・コンポーネントテスト
- [Playwright](https://playwright.dev/) — E2Eテストと所要時間の記録
- [GitHub Actions](https://docs.github.com/ja/actions) — CIでの実行と時間の記録
- [storycap](https://github.com/reg-viz/storycap) — 全Storyのスクリーンショット取得
- [reg-suit](https://github.com/reg-viz/reg-suit) — スクリーンショット差分の検出と報告（OSS）
- [MagicPod](https://magicpod.com/) — ノーコードのE2Eテスト自動化（商用）
- [GitLab CI/CD](https://docs.gitlab.com/ci/) — GitLabでのパイプライン実行

**関連する要素技術**

- [テスト設計](../skills/quality/test.design.md)、[単体テスト](../skills/quality/test.unit.md)、[コンポーネントテスト](../skills/quality/test.component.md)、[E2Eテスト](../skills/quality/test.e2e.md)、[フロントエンド品質保証](../skills/quality/frontend.quality.md)

<!-- references:end -->
