---
title: "TypeScript"
description: "TypeScriptの型でプログラムの入出力と状態を表現する要素技術です。ユニオン型や型の絞り込みを使い、外部データの実行時確認と型定義を整合させ、あり得ない状態を型で防げるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# TypeScript

**要素技術ID：** `typescript.basic`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** JavaScript

TypeScriptの型でプログラムの入出力と状態を表現する要素技術です。ユニオン型や型の絞り込みを使い、外部データの実行時確認と型定義を整合させ、あり得ない状態を型で防げるかを評価します。

## Lv0

型注釈やコンパイル時の検査の役割を説明できず、単純な型エラーの修正にも手順ごとの指示が必要である。

## Lv1

例や支援に沿って変数・関数・オブジェクトの型を定義し、単純な型エラーを修正できる。型検査の実行結果を確認できる。

## Lv2

ユニオン型、型の絞り込み、ジェネリクスの基本を使って入出力を表現できる。安易なanyや型アサーションを避け、外部データには実行時の確認が必要であることを説明できる。

## Lv3

複雑な状態やライブラリ境界の型を設計し、存在してはいけない状態の組み合わせを型で抑制できる。型の複雑さと利用しやすさを比較し、型エラーと実行時不具合の両面から改善できる。

## Lv4

型設計の規約、公開インターフェース、型検査設定、例外の扱いをチームへ展開できる。移行や教育を支援し、型関連の不具合と回避コードの減少を確認できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) — 公式ハンドブック（英語）
- [サバイバルTypeScript](https://typescriptbook.jp/) — 実務向けの入門書（日本語、OSS）
- [TypeScript Deep Dive（日本語版）](https://typescript-jp.gitbook.io/deep-dive) — 型システムの詳細解説

**代表的なライブラリ・ツール**

- [TypeScript](https://www.typescriptlang.org/) — 公式サイトとPlayground
- [typescript-eslint](https://typescript-eslint.io/) — TypeScript向けの静的検査
- [tsc（コンパイラオプション）](https://www.typescriptlang.org/ja/tsconfig/) — strict設定などの構成

<!-- references:end -->
