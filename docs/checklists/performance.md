---
title: "パフォーマンス"
description: "Webフロントエンド版DX Criteria 2-1「パフォーマンス」（ユーザー体験を支える品質）の4項目。メトリクスの計測、学習と改善、プラクティス、アンチパターンの原文と補足、架空の回答例。"
titleTemplate: ":title | チームチェック | 習熟度ガイド"
---

# パフォーマンス

**出典：** [Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)（一般社団法人日本CTO協会、CC BY-SA 4.0）  
**大テーマ：** 2. ユーザー体験を支える品質  
**小テーマ：** 2-1 パフォーマンス

<!-- terms:start -->

**前提となる用語：** [Webパフォーマンス](../guide/glossary.md#webパフォーマンス)、[Core Web Vitals](../guide/glossary.md#core-web-vitals)、[Lighthouse](../guide/glossary.md#lighthouse)、[モニタリングとオブザーバビリティ](../guide/glossary.md#モニタリングとオブザーバビリティ)、[SLO](../guide/glossary.md#slo)  
**関連する要素技術：** [Webパフォーマンス](../skills/quality/web.performance.md)、[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)

<!-- terms:end -->

<ClientOnly><TeamAssessment /></ClientOnly>

## 2-1-1：メトリクスの計測

Core Web Vitalsやプロダクトのコアな価値に通じる速度指標についてパフォーマンス計測を週1回以上の頻度で自動的に計測している。

::: supplement
動画メディアであればメディアコンテンツが視聴可能になるまでの時間を User Timings API で収集するなどが考えられる。
:::

::: example
- 主要画面の表示時間や主要操作の応答時間を、代表的なデータ量・端末・ネットワーク条件で週1回以上自動計測しています。
- Core Web Vitalsを利用する場合は、実利用データと試験環境の計測値を区別しています。
- 計測条件・対象バージョン・結果を保存し、前回からの悪化を検出しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/473c35c88afc4360a38cba2df5033a18)

## 2-1-2：学習と改善

速度指標やアセットサイズ指標の計測結果をチーム内で共有し、アクションプランを定期的（月ごと〜半年ごと）に検討している。

::: example
- 主要画面の速度指標とJavaScript・CSS・画像などの転送サイズをダッシュボードで共有しています。
- 月次で目標値との差と増加要因を確認し、利用者への影響が大きい項目から改善計画を作成しています。
- 担当者と完了条件を定め、対応後の計測で効果を確認しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/bb370a1076c849d798c98ccf4873214f)

## 2-1-3：プラクティス

Synthetic MonitoringやReal User Monitoringに対応したパフォーマンス計測サービス（SpeedCurve、New Relic など）か同様の仕組みで任意の指標を常時計測している。

::: example
- 本番環境の主要な利用経路について、定期的な自動操作による監視と、取得可能な範囲の実利用時の性能データを継続的に収集しています。
- 画面・端末・リリース単位で応答時間とエラーを確認できます。
- 計測の停止やデータ欠損も検知し、監視が継続していることを確認しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/d893af17bd704b6ea4eaf66d30024c54)

## 2-1-4：アンチパターン

目標やアラートを設定していないことによって、過度に最適化したり、運用中に生じた性能劣化を見過ごしたりしてしまっている。

::: example
- 主要操作の性能目標と悪化を検知するアラートを設定しており、目標不在による過度な最適化や性能劣化の見逃しを防いでいます。
- 改善は目標との差と利用者への影響で優先順位を決めています。
- アラート発生時の担当者・調査手順・対応期限を定め、検知結果と対応を記録しています。
:::

[原文の参照先](https://dxcriteria.cto-a.org/dc6c2f9f23ba45768a87e0219e745174)

## 参考リンク

<!-- references:start -->

参考資料であり、採用の推奨ではありません。出典の項目文で言及されているものには（出典で言及）と付記しています。選定は[技術選定](technology-selection.md)の観点で行ってください。2026年9月確認。

**指針・標準**

- [web.dev：Core Web Vitals](https://web.dev/articles/vitals?hl=ja) — 速度指標の定義
- [MDN：User Timing](https://developer.mozilla.org/ja/docs/Web/API/Performance_API/User_timing)（出典で言及） — 独自の速度指標の計測
- [Chrome UX Report](https://developer.chrome.com/docs/crux?hl=ja) — 実利用データの公開情報

**代表的なツール・サービス**

- [SpeedCurve](https://www.speedcurve.com/)（出典で言及） — Synthetic／Real User Monitoring
- [New Relic](https://newrelic.com/jp)（出典で言及） — 性能監視サービス
- [Lighthouse](https://developer.chrome.com/docs/lighthouse?hl=ja) — 試験環境での自動計測
- [PageSpeed Insights](https://pagespeed.web.dev/) — 実利用データを含む診断
- [web-vitals](https://github.com/GoogleChrome/web-vitals) — 実利用の指標を計測するライブラリ

<!-- references:end -->
