---
title: "Webセキュリティ"
description: "Webアプリケーションの代表的なリスクを理解し、対策を実装する要素技術です。XSS、CSRF、認可漏れ、機密情報の露出を実装箇所と結び付け、データの流れと信頼境界から脅威を評価できるかを評価します。"
titleTemplate: ":title | 要素技術 | 習熟度ガイド"
---

# Webセキュリティ

**要素技術ID：** `web.security`  
**領域：** [品質・高度化領域](index.md)  
**主な前提：** Web基礎、JavaScript、API連携

<!-- terms:start -->

**前提となる用語：** [脆弱性](../../guide/glossary.md#脆弱性)、[XSS](../../guide/glossary.md#xss)、[CSP](../../guide/glossary.md#csp)、[クロスオリジンとCORS](../../guide/glossary.md#クロスオリジンとcors)、[機密情報とシークレット管理](../../guide/glossary.md#機密情報とシークレット管理)、[認証と認可](../../guide/glossary.md#認証と認可)

<!-- terms:end -->

Webアプリケーションの代表的なリスクを理解し、対策を実装する要素技術です。XSS、CSRF、認可漏れ、機密情報の露出を実装箇所と結び付け、データの流れと信頼境界から脅威を評価できるかを評価します。

::: start
IPAの「安全なウェブサイトの作り方」で、XSSなど代表的な脆弱性の仕組みと対策を読みます。自分の画面で利用者の入力をそのままHTMLに出している箇所を探し、エスケープや検証で直せれば、Lv1の入口です。まず読む：[IPA：安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity.html)
:::

## Lv0

入力・出力、認証・認可、機密情報、信頼できないデータの区別を説明できず、安全な実装の確認に手順ごとの指示が必要である。

## Lv1

開発ガイドに沿って安全な出力方法や機密情報の扱いを確認し、既存の認証・認可の仕組みを利用できる。検査の指摘は支援を受けて確認・修正できる。

## Lv2

XSS、CSRF、認可漏れ、機密情報の露出などの代表的なリスクを実装箇所と結び付けて説明できる。承認された方式で対策し、クライアント側の制御だけで保護を完結させず、サーバー側の検証と併せて確認できる。

## Lv3

データの流れと信頼境界から脅威を整理し、認証情報、外部スクリプト、依存関係、API連携のリスクを評価できる。許可された検証環境で問題を再現・修正し、専門担当者に相談すべき範囲を判断できる。

## Lv4

実装基準、共通対策、静的検査・依存関係検査、例外管理、教育、脆弱性対応の手順を関係者と整備できる。チームでの運用実績を基に、指摘の再発と修正までの時間を改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — 代表的なリスクの一覧（英語）
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 対策の実装指針（英語）
- [MDN：Webセキュリティ](https://developer.mozilla.org/ja/docs/Web/Security) — ブラウザのセキュリティ機構の解説
- [MDN：Content Security Policy](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/CSP) — スクリプト実行の制限
- **まず読む** [IPA：安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity.html) — 脆弱性別の対策（日本語）

**代表的なライブラリ・ツール**

- [GitHub code scanning](https://docs.github.com/ja/code-security/code-scanning) — PRごとの静的検査
- [Dependabot](https://docs.github.com/ja/code-security/dependabot) — 依存関係の脆弱性検知と更新
- [DOMPurify](https://github.com/cure53/DOMPurify) — HTMLのサニタイズ

<!-- references:end -->
