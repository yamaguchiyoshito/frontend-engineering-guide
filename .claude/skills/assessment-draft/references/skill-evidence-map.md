# 要素技術ごとの手がかり

`collect_evidence.py` の出力（`skills` セクション：触れたファイル数、コミット例、内容の手がかり）を、各要素技術のLvの候補に読み替えるための対応表。右端の「上限」は、リポジトリの事実だけで到達できるLvの目安。それより上は面談・レビューで確認する候補とする。

| 要素技術 | リポジトリの手がかり | Lv1〜Lv2を示す例 | 上限 |
| :--- | :--- | :--- | :--- |
| `web.basic` Web基礎 | fetch／ヘッダー／Cookie／キャッシュ制御の実装、`next.config` の `headers()`、HTTPエラー処理 | 再試行・タイムアウト・ステータス別処理を自分で実装・検証 | Lv2 |
| `html.basic` HTML | `.html`、JSXの構造、フォーム要素、`label`／`htmlFor` | 画面やフォームを一から作った変更 | Lv2 |
| `css.basic` CSS | `.css`／`.scss`、ユーティリティクラス、ボックスモデル・配置の変更 | 新規画面のレイアウトを実装し崩れを修正 | Lv2 |
| `javascript.basic` JavaScript | `.js`／`.ts` のロジック、配列・オブジェクト操作、例外処理 | 要件を関数に分解した実装とそのテスト | Lv2 |
| `git.basic` Git | コミットの粒度とメッセージ、revert、ブランチ運用 | 作業単位で分けたコミット、競合解消のマージ | Lv2 |
| `html.semantic` セマンティックHTML | `main`／`nav`／`header`／`section`、見出し階層、ランドマーク | 意味に沿った要素選択を伴う画面実装 | Lv2 |
| `css.responsive` レスポンシブ設計 | `@media`／`@container`／`clamp`／Grid・Flex、Tailwind のブレークポイント接頭辞 | 複数幅で確認した切り替えの実装 | Lv2 |
| `javascript.dom` DOM・イベント操作 | `addEventListener`、`querySelector`、フォーカス制御、イベント伝播 | 動的要素・フォーカス移動を扱う実装 | Lv2 |
| `javascript.async` 非同期処理 | `await`、`Promise.all`、`AbortController`、再試行、競合対策 | 読み込み中・成功・失敗の状態を扱う実装 | Lv2 |
| `typescript.basic` TypeScript | `.ts`／`.tsx` の型定義、ジェネリクス、`any`／`@ts-ignore` の少なさ、`strict` | 型で境界を表現した実装、`any` の回避 | Lv2 |
| `web.accessibility` Webアクセシビリティ | `aria-*`、`role`、`alt`、`lang`、`vitest-axe`／`jest-axe`／`eslint-plugin-jsx-a11y`、キーボード操作 | 支援技術を想定した実装とaxe検査 | Lv2 |
| `web.seo` SEO | `metadata`／`generateMetadata`、`robots.txt`、`sitemap`、OGタグ、正規URL | メタデータの設計と確認 | Lv2 |
| `git.collaboration` チーム開発 | `.github/`、PRテンプレート、CODEOWNERS、マージコミット、`Co-authored-by`、レビュー慣行の設定 | PRの作成・修正・マージの繰り返し | Lv2（レビューの質はLv3の確認事項） |
| `react.basic` React実装 | `.tsx`／`.jsx` のコンポーネント、props、state、Hooks | 一覧・詳細・状態更新を伴う画面の実装 | Lv2 |
| `react.component-design` コンポーネント設計 | 共通部品と画面固有部品の分離、公開インターフェース、`components/` の構成 | 責務を分けた部品化の変更 | Lv2（境界の設計判断はLv3の確認事項） |
| `react.state-management` 状態管理 | `useReducer`、`createContext`、Zustand／Redux／Jotai、サーバー状態（TanStack Query／SWR） | ローカル・共有・サーバー状態を区別した実装 | Lv2 |
| `react.form` フォーム実装 | `react-hook-form`、`<form>`、エラー表示、送信状態 | 登録・編集フォームと検証・エラー表示の実装 | Lv2 |
| `frontend.validation` 入力検証 | Zod／Yup／Valibot のスキーマ、サーバー側との共有、エラーメッセージ | スキーマで入力を検証する実装 | Lv2 |
| `frontend.api-integration` REST API連携 | `fetch`／`axios`、TanStack Query、OpenAPI生成（orval 等）、MSW のハンドラ | 取得・更新・エラー・キャッシュを扱う実装 | Lv2 |
| `storybook.basic` Storybook | `.stories.*`、`.storybook/`、addon（a11y、vitest） | 状態ごとのストーリーを整備 | Lv2 |
| `nextjs.routing` App Routerによる画面構成 | `app/**/page|layout|loading|error|not-found`、動的ルート、`next/link`、`redirect` | レイアウト・動的ルート・遷移を含む画面群の実装 | Lv2 |
| `nextjs.rendering` レンダリングとデータ取得 | `'use client'`／`'use server'`、`revalidate*`、Server Actions、`Suspense`、`fetch` のキャッシュ指定 | 境界を決めてデータ取得と更新を実装 | Lv2 |
| `frontend.styling` スタイリング設計 | Tailwind の設定・テーマ、CSS変数、デザイントークン、`cva`、shadcn/ui のテーマ | バリエーション・ダークモードをテーマで実装 | Lv2 |
| `test.unit` ユニットテスト | `*.test.*`／`*.spec.*`、Vitest／Jest の設定、カバレッジ設定 | 境界値・例外を含むテストの追加 | Lv2 |
| `test.component` コンポーネントテスト | `@testing-library`、ユーザー操作の検証、`vitest-axe` | 操作と表示を検証するテスト | Lv2 |
| `test.integration` 結合テスト | MSW、複数部品・API連携のテスト、`integration` ディレクトリ | API連携を含む結合テストの実装 | Lv2 |
| `test.e2e` E2Eテスト | `@playwright/test`／Cypress、`e2e/`、CI での実行、シャーディング | 主要導線のE2Eと安定化 | Lv2 |
| `test.design` テスト設計 | テストの観点・境界値・異常系の網羅、テスト方針の文書 | 観点に沿って分類されたテスト群 | Lv2（方針の整備はLv3〜Lv4の確認事項） |
| `web.performance` Webパフォーマンス | `next/image`、動的インポート、Lighthouse CI、`web-vitals`、バンドル分析、キャッシュ | 計測して改善した変更（前後の数値がコミットやPRに残る） | Lv2 |
| `web.security` Webセキュリティ | CSP、`dangerouslySetInnerHTML` の有無とサニタイズ、認証・認可の扱い、依存関係の監査、機密情報の扱い | 検査の指摘を修正、安全な出力の実装 | Lv2 |
| `frontend.quality` フロントエンド品質保証 | ESLint／Prettier／型検査／テストのCI、lint-staged、ブランチ保護を前提とした設定 | 検査を導入・修正し、CIで維持 | Lv2（規約の整備と定着はLv4の確認事項） |

## 共通の注意

- 「導入している」は Lv1 の根拠。「要件に合わせて実装し、検証・修正まで完結」が Lv2 の根拠。「複数案の比較、原因分析、構成の改善、他者のレビュー」が Lv3、「規約・共通部品・自動検査・教材の整備と、他者の利用と改善効果の確認」が Lv4 の根拠で、後二者はPRの議論、レビュー、運用の実績が要る。
- 対象者が触れたファイル数が多くても、他者のコードの軽微な修正や機械的な置換（リネーム、フォーマット）は根拠から除く。コミット例の内容を `git show --stat` で確認する。
- 一つのコミット例は複数の要素技術の根拠になり得るが、同じ根拠で3つ以上の要素技術をLv2にしない。それぞれの要素技術の定義文に対応する行動を確認する。
