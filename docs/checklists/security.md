---
title: "セキュリティ"
description: "Webフロントエンド版DX Criteria 2-3「セキュリティ」（ユーザー体験を支える品質）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# セキュリティ

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 2. ユーザー体験を支える品質  
**小テーマ：** 2-3 セキュリティ

<!-- terms:start -->

**前提となる用語：** [脆弱性](../guide/glossary.md#脆弱性)、[SAST](../guide/glossary.md#sast)、[CI](../guide/glossary.md#ci)、[サプライチェーン](../guide/glossary.md#サプライチェーン)、[依存関係の更新検知](../guide/glossary.md#依存関係の更新検知)、[機密情報とシークレット管理](../guide/glossary.md#機密情報とシークレット管理)  
**関連する要素技術：** [Webセキュリティ](../skills/quality/web.security.md)、[REST API連携](../skills/implementation/frontend.api-integration.md)、[フロントエンド品質保証](../skills/quality/frontend.quality.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 2-3-1：メトリクスの計測

SASTに相当する静的検査がPull Requestごとに実行されて一定の基準を満たさないコードが混入しない仕組みになっている。

**補足**

SAST（Static Application Security Testing）相当のソリューションは各所から提供されており、身近な例ではGitHub Code Scanningなどがある。

::: example
PRごとにSASTをCIで実行し、検査対象と重大度ごとの許容基準を定めています。必須基準に違反した場合や検査自体が失敗した場合はマージを停止します。誤検知や例外は理由・承認者・有効期限を記録し、修正または再評価まで追跡しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/db9f70c9c291474b84c1961d8d656560)

## 2-3-2：学習と改善

Webのセキュリティと開発時の注意事項について、開発者を対象とした教育カリキュラムや研修を実施して知識のアップデートを促している。

::: example
開発者の参加時と半年ごとに、Webセキュリティの研修を実施しています。入力処理、認証・認可、機密情報の扱い、依存関係などを題材に、脆弱な実装と修正方法を演習で確認しています。受講履歴と理解度を記録し、実際の指摘や新たな脅威を教材と開発ガイドに反映しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/7c88f442f7ae4bf198862d5968485e3b)

## 2-3-3：プラクティス

DependabotやRenovateなどのサプライチェーン脆弱性を検知できる仕組みを利用して、緊急度に応じた期間内にアップデートを適用できている。

::: example
依存関係の脆弱性検査と更新検知を組み合わせ、直接・間接依存の問題を継続的に確認しています。重大度、悪用の有無、利用箇所への到達可能性から緊急度を判断し、事前に定めた期限内に更新と動作検証を行っています。修正版がない場合は暫定対策を実施し、解消まで担当者が追跡しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/90cf6080f31b47d395ce12d5121efb35)

## 2-3-4：アンチパターン

ソースコード中にクレデンシャル等の機密情報がハードコーディングされている。

**補足**

ソースコードは開発者のローカルにコピーが作成されたあとの管理不備や、リポジトリ管理サービスの読み取り権限の漏洩等で暴露されてしまう危険性が高い傾向にある。

JavaScriptバンドルやHTMLを経由してクライアントサイドに露出する前提のAPIキーなどは制限の対象から外せるが、Secrets Managerなどの運用を前提に一元的に扱うほうが多くの場合で管理上のメリットを得られる。

Secrets Managerなどを経由してビルド時や実行時に環境変数として注入する手法が一般的である。

::: example
パスワード、秘密鍵、非公開のAPIキーなどをソースコードに埋め込んでいません。機密情報はシークレット管理機構で保管し、権限を限定して実行時に渡しています。コミットやCIで混入を検査し、検出時は削除に加えて失効・再発行と影響調査を行います。ブラウザへ配布するコードにも秘密情報を含めていません。
:::

[原文の参照先](https://dxcriteria.cto-a.org/a11bd8821047430bbb6c37d4002d504e)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — 代表的なリスク（英語）
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 対策の実装指針（英語）
- [IPA：安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity.html) — 脆弱性別の対策と教育資料

**代表的なツール・サービス**

- [GitHub code scanning](https://docs.github.com/ja/code-security/code-scanning)（出典で言及） — PRごとの静的検査
- [Dependabot](https://docs.github.com/ja/code-security/dependabot)（出典で言及） — サプライチェーン脆弱性の検知
- [Renovate](https://docs.renovatebot.com/)（出典で言及） — 依存関係の自動更新
- [gitleaks](https://github.com/gitleaks/gitleaks) — 機密情報の混入検査

<!-- references:end -->
