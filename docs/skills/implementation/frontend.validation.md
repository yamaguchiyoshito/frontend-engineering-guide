---
title: "入力検証・型連携"
description: "入力値の検証を実装し、型定義とAPIの入出力を整合させる要素技術です。スキーマで空値、型変換、境界値、メッセージを扱い、フロントエンドとサーバー側の検証責務を区別できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# 入力検証・型連携

**要素技術ID：** `frontend.validation`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** フォーム、TypeScript

<!-- terms:start -->

**前提となる用語：** [入力検証](../../guide/glossary.md#入力検証)、[スキーマ](../../guide/glossary.md#スキーマ)、[TypeScript](../../guide/glossary.md#typescript)、[OpenAPI](../../guide/glossary.md#openapi)

<!-- terms:end -->

入力値の検証を実装し、型定義とAPIの入出力を整合させる要素技術です。スキーマで空値、型変換、境界値、メッセージを扱い、フロントエンドとサーバー側の検証責務を区別できるかを評価します。

::: start
Zodの公式ドキュメントで、スキーマの定義と検証の書き方を読みます。フォームの入力値をスキーマで検証し、エラーメッセージを項目ごとに表示できれば、Lv1の入口です。まず読む：[Zod](https://zod.dev/)
:::

## Lv0

入力値の検証と型検査の違い、検証エラーの扱いを説明できず、検証条件の実装に手順ごとの指示が必要である。

## Lv1

例に沿って必須、文字数、数値範囲などの条件を実装し、指定された正常値と異常値で確認できる。型と実行時の検証の対応には支援が必要である。

## Lv2

要件からスキーマを定義し、空値、型変換、境界値、エラーメッセージを実装・検証できる。フロントエンドの検証とサーバー側で必須となる検証を区別し、APIの入出力と整合させられる。

## Lv3

項目間・業務条件・非同期の検証を設計し、型定義と実行時スキーマのずれを検出・修正できる。API仕様変更時の互換性、エラー対応、検証責務を関係者と調整できる。

## Lv4

スキーマの管理・共有方針、型との連携、エラー表現、契約確認の仕組みを整備できる。チームで運用し、検証漏れやフロントエンド・バックエンド間の不一致を減らせる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [MDN：制約検証](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Constraint_validation) — HTML標準の入力検証
- [OWASP：Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — サーバー側で必須となる検証の指針（英語）
- [TypeScript Handbook：Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) — 外部データを型安全に扱う基礎（英語）

**代表的なライブラリ・ツール**

- **まず読む** [Zod](https://zod.dev/) — スキーマ定義と型の導出
- [Valibot](https://valibot.dev/) — 軽量なスキーマ検証ライブラリ
- [openapi-typescript](https://openapi-ts.dev/) — API仕様と型定義の整合
- [openapi-zod-client](https://github.com/astahmer/openapi-zod-client) — OpenAPIからZodスキーマとクライアントを生成

<!-- references:end -->
