---
title: "結合テスト"
description: "画面、状態管理、APIなど複数の部品を結合して検証する要素技術です。結合範囲と実物とモックの境界を明示し、機能横断の状態遷移や部分失敗を検証して障害箇所を切り分けられるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# 結合テスト

**要素技術ID：** `test.integration`  
**領域：** [品質・高度化領域](index.md)  
**主な前提：** React、API連携

画面、状態管理、APIなど複数の部品を結合して検証する要素技術です。結合範囲と実物とモックの境界を明示し、機能横断の状態遷移や部分失敗を検証して障害箇所を切り分けられるかを評価します。

## Lv0

結合対象、境界、データの受け渡し、期待結果を説明できず、単体テストとの違いの整理に支援が必要である。

## Lv1

用意された結合範囲とケースに沿って環境・データを準備し、画面とAPIなどの連携を実行・確認できる。対象範囲と検証内容の設計には支援が必要である。

## Lv2

画面、状態管理、APIなどの結合範囲を明示し、正常系・異常系・データ反映を検証できる。実物とモックの境界を記録し、そのテストで確認できる範囲を説明できる。

## Lv3

機能横断の状態遷移、権限、データ整合性、部分失敗、再実行を含むケースを設計・実装できる。画面・API・ログ・永続化データの観測を組み合わせ、障害箇所を切り分けられる。

## Lv4

結合範囲の決め方、仕様との対応付け、テストデータ、環境、後始末、実行・分析の共通手順を整備できる。他者が再現できる状態へ展開し、結合漏れや調査・再実行工数を減らせる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [Mock Service Worker：ドキュメント](https://mswjs.io/docs/) — APIモックの設計と使い方
- [Playwright：コンポーネントテスト](https://playwright.dev/docs/test-components) — 実ブラウザでの結合検証（実験的機能）
- [Martin Fowler：The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — テスト層の役割分担（英語）

**代表的なライブラリ・ツール**

- [Mock Service Worker](https://mswjs.io/) — 実物とモックの境界の制御
- [Testing Library](https://testing-library.com/) — 画面と状態の検証
- [Playwright](https://playwright.dev/) — ブラウザを使った結合検証

<!-- references:end -->
