---
title: "Git"
description: "Gitで変更履歴を管理する要素技術です。branch、commit、merge、rebaseの操作と違いを理解し、競合の解消や誤った変更からの復旧を、他者の作業に影響を与えずに行えるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# Git

**要素技術ID：** `git.basic`  
**領域：** [基礎領域](index.md)  
**評価対象：** branch、commit、merge、rebase

<!-- terms:start -->

**前提となる用語：** [Git](../../guide/glossary.md#git)、[リポジトリ](../../guide/glossary.md#リポジトリ)、[コミット](../../guide/glossary.md#コミット)、[ブランチ](../../guide/glossary.md#ブランチ)、[マージ](../../guide/glossary.md#マージ)

<!-- terms:end -->

Gitで変更履歴を管理する要素技術です。branch、commit、merge、rebaseの操作と違いを理解し、競合の解消や誤った変更からの復旧を、他者の作業に影響を与えずに行えるかを評価します。

## Lv0

作業ツリー、ステージ、コミット、ブランチの関係を説明できず、変更の保存や取り込みに手順ごとの指示が必要である。

## Lv1

手順に沿ってブランチを作成し、差分確認、ステージング、コミット、pushを実行できる。競合や履歴変更が必要な場合に支援を求められる。

## Lv2

作業内容に応じてコミットを分け、mergeとrebaseの違いを説明してチームの方針に沿って使える。通常の競合を解消し、意図した内容になったことを確認できる。

## Lv3

複雑な競合や誤ったコミットを履歴から調査し、revertなどで安全に復旧できる。共有履歴への影響を判断し、変更の消失や他者の作業への影響を防いで操作できる。

## Lv4

リポジトリの特性に合う履歴管理・競合解消・復旧の標準手順を整備し、演習や支援体制を作れる。他者が手順を使って対応した結果から事故や復旧時間の改善を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [Pro Git（日本語版）](https://git-scm.com/book/ja/v2) — Gitの基本操作と内部構造の解説書
- [Git Reference](https://git-scm.com/docs) — コマンドのリファレンス（英語）
- [GitHub Docs：Gitの使用](https://docs.github.com/ja/get-started/using-git) — 日常的な操作の手順

**代表的なライブラリ・ツール**

- [Git](https://git-scm.com/) — 公式サイトとダウンロード
- [GitHub CLI](https://cli.github.com/) — コマンドラインからのGitHub操作
- [GitHub Desktop](https://desktop.github.com/) — GUIでのGit操作

<!-- references:end -->
