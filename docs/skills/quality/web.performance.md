---
title: "Webパフォーマンス"
description: "画面の表示と操作の速度を計測し、改善する要素技術です。速度指標と計測条件を定めて画像、通信、JavaScript処理、描画のボトルネックを特定し、実利用データに基づく代替案を比較できるかを評価します。"
titleTemplate: ":title | 要素技術 | 開発ガイド"
---

# Webパフォーマンス

**要素技術ID：** `web.performance`  
**領域：** [品質・高度化領域](index.md)  
**主な前提：** HTML、CSS、JavaScript、React

<!-- terms:start -->

**前提となる用語：** [Webパフォーマンス](../../guide/glossary.md#webパフォーマンス)、[Core Web Vitals](../../guide/glossary.md#core-web-vitals)、[Lighthouse](../../guide/glossary.md#lighthouse)、[キャッシュ](../../guide/glossary.md#キャッシュ)、[ビルドとバンドル](../../guide/glossary.md#ビルドとバンドル)、[レンダリング](../../guide/glossary.md#レンダリング)

<!-- terms:end -->

画面の表示と操作の速度を計測し、改善する要素技術です。速度指標と計測条件を定めて画像、通信、JavaScript処理、描画のボトルネックを特定し、実利用データに基づく代替案を比較できるかを評価します。

::: start
web.devの「Core Web Vitals」で、LCP、INP、CLSがそれぞれ何を測るかを読みます。自分の画面をLighthouseで計測し、指摘された項目の意味を説明して一つ改善できれば、Lv1の入口です。まず読む：[web.dev：Core Web Vitals](https://web.dev/articles/vitals?hl=ja)
:::

## Lv0

表示・通信・操作の速度の違いや主な遅延要因を説明できず、性能計測の実行と結果の読み取りに支援が必要である。

## Lv1

指定された条件とツールで表示時間、通信量、処理時間を計測し、結果を記録できる。提示された改善方法を適用して再計測できる。

## Lv2

主要な利用経路の速度指標と計測条件を定め、画像、通信、JavaScript処理、描画などの通常のボトルネックを特定できる。同じ条件で改善前後を比較し、他機能への影響も確認できる。

## Lv3

実利用と試験環境のデータを区別し、端末・ネットワーク・データ量ごとの原因を分析できる。配信、キャッシュ、分割読み込み、描画などの代替案を比較し、複数の制約を踏まえて改善できる。

## Lv4

性能目標、計測条件、継続監視、性能予算、悪化検知と対応の仕組みを整備できる。チームの開発・運用へ組み込み、利用者の所要時間と性能劣化の再発を継続して改善できる。

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。選定は[技術選定](../../checklists/technology-selection.md)の観点で行ってください。2026年9月確認。

**仕様・公式ドキュメント**

- **まず読む** [web.dev：Core Web Vitals](https://web.dev/articles/vitals?hl=ja) — 主要な速度指標の定義
- [MDN：Webパフォーマンス](https://developer.mozilla.org/ja/docs/Web/Performance) — 計測と改善の基礎
- [Chrome DevTools：パフォーマンス](https://developer.chrome.com/docs/devtools/performance?hl=ja) — 処理と描画のプロファイル
- [web.dev：Learn Performance](https://web.dev/learn/performance?hl=ja) — 画像、フォント、リソースヒント、コード分割の体系的な学習コース

**代表的なライブラリ・ツール**

- [Lighthouse](https://developer.chrome.com/docs/lighthouse?hl=ja) — 試験環境での診断
- [PageSpeed Insights](https://pagespeed.web.dev/) — 実利用データを含む診断
- [web-vitals](https://github.com/GoogleChrome/web-vitals) — 実利用の指標を計測するライブラリ
- [WebPageTest](https://www.webpagetest.org/) — 条件を指定した詳細計測（自動到達確認の対象外）
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) — CIでの計測と基準値の判定

<!-- references:end -->
