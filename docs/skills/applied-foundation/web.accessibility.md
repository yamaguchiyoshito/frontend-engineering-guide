---
title: "アクセシビリティ"
description: "多様な利用者と支援技術で画面を操作できるようにする要素技術です。キーボード操作、読み上げ、状態変化の伝達を実装・検証し、自動検査で見つからない障壁を調査して改善できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# アクセシビリティ

**要素技術ID：** `web.accessibility`  
**領域：** [応用基礎領域](index.md)  
**主な前提：** HTML、セマンティックHTML

<!-- terms:start -->

**前提となる用語：** [アクセシビリティ](../../guide/glossary.md#アクセシビリティ)、[WCAG](../../guide/glossary.md#wcag)、[支援技術とスクリーンリーダー](../../guide/glossary.md#支援技術とスクリーンリーダー)、[セマンティックHTML](../../guide/glossary.md#セマンティックhtml)

<!-- terms:end -->

多様な利用者と支援技術で画面を操作できるようにする要素技術です。キーボード操作、読み上げ、状態変化の伝達を実装・検証し、自動検査で見つからない障壁を調査して改善できるかを評価します。

## Lv0

キーボード、読み上げ、色の識別などに関する利用上の障壁を説明できず、基本的な確認に手順ごとの指示が必要である。

## Lv1

チェックリストに沿ってラベル、代替テキスト、キーボード操作、フォーカス表示を確認し、支援を受けて基本的な不備を修正できる。

## Lv2

チームの品質基準に沿って画面を実装し、自動検査とキーボード・読み上げによる確認を行える。入力エラーや状態変化が利用者へ伝わることを検証できる。

## Lv3

モーダル、複合ウィジェット、動的更新などの操作・意味構造・フォーカスを設計できる。自動検査で検出できない障壁も調査し、代替案を比較してレビュー・修正できる。

## Lv4

対象範囲と適合目標、共通UI、検証手順、例外管理、教育を一体で整備できる。利用者による確認やチームの運用実績を基に、障壁の解消と継続的な品質維持を進められる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- [WCAG 2.2（日本語訳）](https://waic.jp/translations/WCAG22/) — Webアクセシビリティの国際規格
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — 複合ウィジェットの操作パターン（英語）
- [MDN：アクセシビリティ](https://developer.mozilla.org/ja/docs/Web/Accessibility) — 実装ガイドとARIAのリファレンス
- [デジタル庁：ウェブアクセシビリティ導入ガイドブック](https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook) — 方針策定と実務の手引き

**代表的なライブラリ・ツール**

- [axe-core](https://github.com/dequelabs/axe-core) — 自動アクセシビリティ検査エンジン
- [Lighthouse](https://developer.chrome.com/docs/lighthouse?hl=ja) — アクセシビリティ監査を含むページ診断
- [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) — JSXの静的検査
- [NVDA](https://www.nvaccess.org/) — Windows向けスクリーンリーダー（無償）

<!-- references:end -->
