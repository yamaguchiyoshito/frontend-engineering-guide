---
title: "サプライチェーン"
description: "Webフロントエンド版DX Criteria 3-4「サプライチェーン」（安定的なデリバリー）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# サプライチェーン

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 3. 安定的なデリバリー  
**小テーマ：** 3-4 サプライチェーン

<!-- terms:start -->

**前提となる用語：** [パッケージと依存関係](../guide/glossary.md#パッケージと依存関係)、[サプライチェーン](../guide/glossary.md#サプライチェーン)、[脆弱性](../guide/glossary.md#脆弱性)、[依存関係の更新検知](../guide/glossary.md#依存関係の更新検知)  
**関連する要素技術：** [Webセキュリティ](../skills/quality/web.security.md)、[チーム開発](../skills/applied-foundation/git.collaboration.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 3-4-1：メトリクスの計測

DependabotやRenovateなど依存ライブラリの更新を検知する仕組みを導入している。

::: supplement
2-3-3 (セキュリティ) でも依存ライブラリに関する自動検知について触れているが、通常のアップデートサイクルとは異なる緊急性の高いアップデート対応でも有効な仕組みである。
:::

::: example
依存ライブラリの新しいバージョンを自動検知する仕組みを導入し、更新内容をPRや通知で確認できるようにしています。実行頻度と対象リポジトリを定め、設定の停止や更新漏れも確認しています。通知には変更内容と互換性への影響を調査できる情報を含めています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/c9255445e39f4102ae1961a3b046a8e6)

## 3-4-2：学習と改善

依存ライブラリについて更新や置き換え、削除などの管理を定期的（月ごと〜半年ごと）に計画、実施できている。

::: supplement
依存ライブラリは放っておくといたずらに肥大化してしまいがちである。例えばアップデートに工数が必要な場合は適切に計画するか、代替手段への置き換えを検討できる。Polyfillなどの類は最新のブラウザ環境であれば不要になっていることもある。

サプライチェーンをマネジメントするという観点で定期的な棚卸しと見直しをすることが望ましい。
:::

::: example
月次で依存ライブラリを棚卸しし、更新、置き換え、削除の計画を作成しています。サポート状況、セキュリティ、利用箇所、代替手段を確認して優先順位を決めています。担当者と期限を設定し、変更後の動作確認と不要な依存関係の削除まで追跡しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/b70b47ffa2634bce85a887d8a46703ed)

## 3-4-3：プラクティス

依存ライブラリの重要度や自チームのリソースを踏まえて、更新の反映サイクルなどをポリシーとして定めている。

::: example
依存ライブラリを重要度と変更リスクで分類し、緊急更新は随時、通常更新は月次、影響の大きい更新は四半期ごとの計画で扱う方針を定めています。対応期限、必要な検証、担当者、自動マージを許可する条件を明文化しています。保守工数を開発計画に含め、方針の実施状況を確認しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/0c9d0dc09aa74c909874bf0b0ec3ae29)

## 3-4-4：アンチパターン

自動的に作成された依存ライブラリの更新Pull Requestが手つかずのまま形骸化してしまっている。

::: supplement
依存ライブラリの更新を検知してPull Requestを自動作成してくれるサービスは便利だが、自信をもってマージできるテスト環境が整っていない等の背景で放置されてしまうと、サプライチェーンのマネジメント自体が形骸化してしまう。

サプライチェーンのプラクティス項でも触れているとおり、優先順位等の戦略をもって自分たちのチームにとって許容できる頻度になるように設定すると良い。
:::

::: example
自動作成された更新PRを週次で確認し、担当者、対応期限、適用・保留・却下の判断を記録しています。保留には理由と再確認日を設定し、滞留期間が基準を超えたものを一覧化しています。大量のPRが処理を妨げる場合は更新のグループ化や生成頻度を見直し、手つかずの状態を放置していません。
:::

[原文の参照先](https://dxcriteria.cto-a.org/60ddfb9cc3f5409792e00fcebeeb5734)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [OWASP：Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html) — 依存関係の管理と検証の指針（英語）
- [npm Docs：npm audit](https://docs.npmjs.com/cli/v10/commands/npm-audit) — 依存関係の脆弱性の確認
- [OpenSSF Scorecard](https://scorecard.dev/) — 依存先の保守状況の評価（英語）
- [pnpm Docs：pnpm audit](https://pnpm.io/ja/cli/audit) — pnpmでの依存関係の脆弱性の確認

**代表的なツール・サービス**

- [Dependabot](https://docs.github.com/ja/code-security/dependabot)（出典で言及） — 更新検知と自動PR
- [Renovate](https://docs.renovatebot.com/)（出典で言及） — 更新ポリシーを細かく設定できる自動更新
- [Socket](https://socket.dev/) — 依存パッケージの供給元リスクの検査（自動到達確認の対象外）
- [GitHub Advisory Database](https://github.com/advisories) — 脆弱性情報の検索
- [Trivy](https://trivy.dev/) — 依存関係とコンテナイメージの脆弱性スキャン（OSS）

<!-- references:end -->
