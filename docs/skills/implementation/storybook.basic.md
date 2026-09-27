---
title: "Storybook"
description: "Storybookでコンポーネントの状態と振る舞いをカタログ化する要素技術です。主要な状態、境界値、操作をStoryとして記述し、画面に近い構成や非同期処理を再現して実装との不整合を発見できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# Storybook

**要素技術ID：** `storybook.basic`  
**領域：** [フレームワーク・実装領域](index.md)  
**主な前提：** React、コンポーネント設計

Storybookでコンポーネントの状態と振る舞いをカタログ化する要素技術です。主要な状態、境界値、操作をStoryとして記述し、画面に近い構成や非同期処理を再現して実装との不整合を発見できるかを評価します。

## Lv0

Storyの役割と対象コンポーネントの関係を説明できず、既存カタログの起動や確認に個別の指示が必要である。

## Lv1

手順に沿ってStorybookを起動し、既存Storyのpropsや表示例を変更できる。支援を受けて単純なコンポーネントのStoryを追加できる。

## Lv2

コンポーネントの主要な状態・境界値・操作をStoryとして記述し、必要なプロバイダーやモックを設定できる。利用者が用途と振る舞いを確認できる説明を追加できる。

## Lv3

画面に近い構成、非同期処理、エラー、インタラクションを再現し、実装との不整合を発見できる。表示・操作の検証を組み込み、カタログの重複や保守負担を改善できる。

## Lv4

Storyの作成・更新・公開の規約とCI検証を整備し、設計・レビュー・テストで利用する運用を作れる。他者による利用と更新状況を確認し、仕様認識のずれや確認工数を改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [Storybook：ドキュメント](https://storybook.js.org/docs) — 設定、Story、アドオンの公式ガイド
- [Storybook：インタラクションテスト](https://storybook.js.org/docs/writing-tests/interaction-testing) — Story上での操作と検証
- [Storybook：Autodocs](https://storybook.js.org/docs/writing-docs/autodocs) — Storyからの文書生成
- [Storybook：Vitest addon](https://storybook.js.org/docs/writing-tests/integrations/vitest-addon) — StoryをVitestのテストとして実行
- [Storybook：アクセシビリティテスト](https://storybook.js.org/docs/writing-tests/accessibility-testing) — Story上でのaxe検証

**代表的なライブラリ・ツール**

- [Storybook](https://storybook.js.org/) — コンポーネントのカタログと検証環境
- [msw-storybook-addon](https://github.com/mswjs/msw-storybook-addon) — Story内でのAPIモック
- [Chromatic](https://www.chromatic.com/) — ビジュアルリグレッションテスト（商用）。OSSの代替はstorycap＋reg-suit
- [@storybook/addon-designs](https://storybook.js.org/addons/@storybook/addon-designs) — StoryにFigmaのデザインを並べて表示
- [storycap](https://github.com/reg-viz/storycap) — 全Storyのスクリーンショット取得
- [reg-suit](https://github.com/reg-viz/reg-suit) — スクリーンショット差分の検出と報告（OSS）

<!-- references:end -->
