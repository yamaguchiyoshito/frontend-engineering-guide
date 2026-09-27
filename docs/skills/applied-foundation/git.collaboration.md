---
title: "チーム開発"
description: "Pull Requestとレビューを通じてチームで開発を進める要素技術です。レビュー可能な単位で変更を分け、CIの確認と指摘対応を行い、複数人・複数ブランチの変更を調整できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# チーム開発

**要素技術ID：** `git.collaboration`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** Git

Pull Requestとレビューを通じてチームで開発を進める要素技術です。レビュー可能な単位で変更を分け、CIの確認と指摘対応を行い、複数人・複数ブランチの変更を調整できるかを評価します。

## Lv0

PR／MR、レビュー、承認、保護ブランチの役割を説明できず、チームの変更手順を進めるために個別の指示が必要である。

## Lv1

テンプレートと支援に沿ってPR／MRを作成し、変更理由と確認結果を記載できる。レビュー指摘を反映し、CI結果を確認できる。

## Lv2

レビュー可能な単位で変更を分け、説明、セルフレビュー、CI確認、指摘対応、マージまで進められる。他者の変更も目的・影響・確認結果からレビューできる。

## Lv3

複数人・複数ブランチにまたがる変更を調整し、依存関係、競合、段階的な取り込みを管理できる。レビュー停滞や責任の不明確さを分析し、運用を改善できる。

## Lv4

ブランチ方針、レビュー基準、承認・保護設定、CIとの連携、参加者向けガイドを整備できる。チームで運用し、変更の滞留時間や手戻りの改善を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [GitHub Docs：Pull Request](https://docs.github.com/ja/pull-requests) — PRの作成、レビュー、マージの手順
- [Google Engineering Practices：Code Review](https://google.github.io/eng-practices/review/) — コードレビューの指針（英語）
- [Conventional Commits（日本語）](https://www.conventionalcommits.org/ja/) — コミットメッセージの規約
- [Pro Git：ブランチ](https://git-scm.com/book/ja/v2/Git-のブランチ機能-ブランチとは) — ブランチ運用の基礎

**代表的なライブラリ・ツール**

- [GitHub CLI](https://cli.github.com/) — コマンドラインからのPR操作
- [GitHub Actions](https://docs.github.com/ja/actions) — CIの設定

<!-- references:end -->
