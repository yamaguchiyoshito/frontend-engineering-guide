---
title: "要素技術"
description: "31の要素技術の一覧。4つの領域ごとに要素技術ID、評価対象または主な前提を示し、各要素技術のLv0〜Lv4の定義へ進めます。"
---

# 要素技術

要素技術は4つの領域に分類します。領域は資格の序列ではなく、担当業務と前提知識に応じて組み合わせるためのまとまりです。

学ぶ順路と教材は[学習コンテンツ](../guide/learning.md)を参照してください。各要素技術にはLv0〜Lv4の到達状態を定義しています。根拠が足りない場合の「未評価」はLv0と区別します。[個人の評価方法](../guide/individual-assessment.md)と併せて確認してください。

<!-- catalog:start -->

## 基礎領域（5つの要素技術）

| ID | 要素技術 | 評価対象 |
| :--- | :--- | :--- |
| `web.basic` | [Web基礎](foundation/web.basic.md) | HTTP、URL、ブラウザ、Cookie、キャッシュ |
| `html.basic` | [HTML](foundation/html.basic.md) | 文書構造、フォーム、基本要素 |
| `css.basic` | [CSS](foundation/css.basic.md) | セレクタ、ボックスモデル、レイアウト |
| `javascript.basic` | [JavaScript](foundation/javascript.basic.md) | 構文、関数、オブジェクト、配列 |
| `git.basic` | [Git](foundation/git.basic.md) | branch、commit、merge、rebase |

## 応用基礎領域（8つの要素技術）

| ID | 要素技術 | 主な前提 |
| :--- | :--- | :--- |
| `html.semantic` | [セマンティックHTML](applied-foundation/html.semantic.md) | HTML |
| `css.responsive` | [レスポンシブ設計](applied-foundation/css.responsive.md) | CSS |
| `javascript.dom` | [DOM・イベント操作](applied-foundation/javascript.dom.md) | JavaScript |
| `javascript.async` | [非同期処理](applied-foundation/javascript.async.md) | JavaScript |
| `typescript.basic` | [TypeScript](applied-foundation/typescript.basic.md) | JavaScript |
| `web.accessibility` | [アクセシビリティ](applied-foundation/web.accessibility.md) | HTML、セマンティックHTML |
| `web.seo` | [基本SEO](applied-foundation/web.seo.md) | HTML、セマンティックHTML |
| `git.collaboration` | [チーム開発](applied-foundation/git.collaboration.md) | Git |

## フレームワーク・実装領域（10の要素技術）

| ID | 要素技術 | 主な前提 |
| :--- | :--- | :--- |
| `react.basic` | [React実装](implementation/react.basic.md) | JavaScript、TypeScript、DOM |
| `react.component-design` | [コンポーネント設計](implementation/react.component-design.md) | React、UI実装 |
| `react.state-management` | [状態管理](implementation/react.state-management.md) | React、非同期処理 |
| `react.form` | [フォーム実装](implementation/react.form.md) | React、TypeScript |
| `frontend.api-integration` | [REST API連携](implementation/frontend.api-integration.md) | 非同期処理、TypeScript |
| `frontend.validation` | [入力検証・型連携](implementation/frontend.validation.md) | フォーム、TypeScript |
| `storybook.basic` | [Storybook](implementation/storybook.basic.md) | React、コンポーネント設計 |
| `nextjs.routing` | [App Routerによる画面構成](implementation/nextjs.routing.md) | React実装、Web基礎 |
| `nextjs.rendering` | [レンダリングとデータ取得](implementation/nextjs.rendering.md) | App Routerによる画面構成、REST API連携、非同期処理 |
| `frontend.styling` | [スタイリング設計](implementation/frontend.styling.md) | CSS、レスポンシブ設計、コンポーネント設計 |

## 品質・高度化領域（8つの要素技術）

| ID | 要素技術 | 主な前提 |
| :--- | :--- | :--- |
| `test.unit` | [単体テスト](quality/test.unit.md) | JavaScript、TypeScript |
| `test.component` | [コンポーネントテスト](quality/test.component.md) | React |
| `test.integration` | [結合テスト](quality/test.integration.md) | React、API連携 |
| `test.e2e` | [E2Eテスト](quality/test.e2e.md) | フォーム、API連携 |
| `test.design` | [テスト設計](quality/test.design.md) | 各テスト実装 |
| `web.performance` | [Webパフォーマンス](quality/web.performance.md) | HTML、CSS、JavaScript、React |
| `web.security` | [Webセキュリティ](quality/web.security.md) | Web基礎、JavaScript、API連携 |
| `frontend.quality` | [フロントエンド品質保証](quality/frontend.quality.md) | テスト設計、性能、セキュリティ |

<!-- catalog:end -->
