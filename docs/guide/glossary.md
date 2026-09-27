---
title: "用語集"
description: "本書の要素技術とチームチェックリストで前提とする用語を、Webとブラウザ、HTML・CSS・JavaScript、チーム開発の流れ、品質・テスト、セキュリティ・運用・チームの5分類で短く説明します。"
---

# 用語集

本書の各ページで説明なしに使っている用語を、フロントエンド開発に不慣れな方向けに短く説明します。各要素技術ページと各小テーマページの冒頭にある「前提となる用語」から、このページの該当する見出しへ移動できます。

ここに載っていない用語は、[MDNの用語集](https://developer.mozilla.org/ja/docs/Glossary)で確認できます。用語の追加や修正は、[編集・検証・公開手順](../maintenance/contributing.md)に沿って `build/glossary.json` を更新してください。

<!-- glossary:start -->

厳密な定義は、各用語の「関連」に示したページと、そのページの参考リンクを参照してください。

## Webとブラウザ

### ブラウザ

Webページを表示するソフトウェアです。Chrome、Safari、Firefoxなどがあります。サーバーから受け取ったHTML・CSS・JavaScriptを解釈して画面を描き、利用者の操作を受け付けます。

関連：[Web基礎](../skills/foundation/web.basic.md)

### サーバー

ブラウザからの要求を受け取り、HTMLやデータを返すコンピューターやプログラムです。利用者の手元で動くブラウザ側をクライアントと呼びます。

### フロントエンドとバックエンド

フロントエンドは利用者のブラウザで動く、画面と操作を担う部分です。バックエンドはサーバーで動く、データの処理・保存・認証などを担う部分です。両者はAPIを通じてやり取りします。

関連：[フロントエンド開発の前提知識](prerequisites.md)

### HTTP

ブラウザとサーバーが情報をやり取りするときの約束事（プロトコル）です。ブラウザが要求（リクエスト）を送り、サーバーが応答（レスポンス）を返します。通信を暗号化したものがHTTPSです。

関連：[Web基礎](../skills/foundation/web.basic.md)

### リクエストとレスポンス

ブラウザからサーバーへの要求と、それに対する返答です。要求にはURLとメソッド（GETは取得、POSTは送信など）が含まれ、返答には結果を示すステータスコードと本文が含まれます。

関連：[Web基礎](../skills/foundation/web.basic.md)

### ステータスコード

レスポンスに含まれる3桁の数字で、要求の結果を表します。200は成功、301や302は別の場所への移動（リダイレクト）、404は見つからない、500はサーバー側の失敗です。

### URL

Web上の場所を示す文字列です。`https://example.com/docs?page=2#top` のように、方式、ホスト名、パス、クエリ（?以降）、フラグメント（#以降）で構成されます。

関連：[Web基礎](../skills/foundation/web.basic.md)

### Cookie

サーバーの指示でブラウザが保存し、次回以降の要求に自動で付ける小さなデータです。ログイン状態の維持などに使います。利用者の追跡にも使われるため、プライバシーの配慮が必要です。

関連：[Web基礎](../skills/foundation/web.basic.md)、[2-4 プライバシー](../checklists/privacy.md)

### キャッシュ

一度取得したファイルやデータを手元に保存し、次回は取得を省いて速く表示する仕組みです。ブラウザ、CDN、サーバーなど複数の層にあり、古い内容が表示され続ける原因にもなります。

関連：[Web基礎](../skills/foundation/web.basic.md)、[4-3 キャッシュ](../checklists/caching.md)

### CDN

Content Delivery Network。利用者に近い場所に配置した配信サーバー群です。画像、CSS、JavaScriptなどの静的ファイルを速く届け、元のサーバーの負荷を減らします。

関連：[4-2 インフラ](../checklists/infrastructure.md)

### クロスオリジンとCORS

表示中のページと異なるドメイン（オリジン）のサーバーへ通信することをクロスオリジンと呼びます。ブラウザは安全のためこれを制限しており、通信先のサーバーが許可を宣言する仕組みがCORSです。

関連：[Web基礎](../skills/foundation/web.basic.md)、[Webセキュリティ](../skills/quality/web.security.md)

### API

Application Programming Interface。プログラム同士が決められた形式でやり取りするための窓口です。フロントエンドはAPIを呼び出して、バックエンドからデータを取得・更新します。

関連：[REST API連携](../skills/implementation/frontend.api-integration.md)

### REST API

URLとHTTPメソッドで「どの資源に何をするか」を表現するAPIの設計様式です。例えば `GET /users/1` は利用者1の情報を取得する、という意味になります。

関連：[REST API連携](../skills/implementation/frontend.api-integration.md)

### JSON

データを `{"name": "山田"}` のような文字列で表す形式です。APIの送受信で広く使われ、JavaScriptからそのまま扱えます。

### OpenAPI

APIの仕様（URL、入力と出力の形）を、機械が読める形式で記述する規格です。仕様から型定義、モック、通信用のコードを自動生成でき、フロントエンドとバックエンドの認識のずれを防ぎます。

関連：[REST API連携](../skills/implementation/frontend.api-integration.md)、[4-1 サーバー](../checklists/backend-collaboration.md)

### 認証と認可

認証は、相手が誰かを確認すること（ログイン）です。認可は、その相手に何を許すかを判断すること（権限）です。両者を分けて考えます。

関連：[Webセキュリティ](../skills/quality/web.security.md)

### レンダリング

ブラウザがHTML・CSS・JavaScriptから画面を描く処理です。サーバー側でHTMLを組み立てて返す方式をSSR、ブラウザ側でJavaScriptが組み立てる方式をCSRと呼びます。

関連：[Webパフォーマンス](../skills/quality/web.performance.md)

## HTML・CSS・JavaScript

### HTML

見出し、段落、リンク、画像、フォームなど、ページの構造と内容を記述する言語です。要素は `<p>…</p>` のようなタグで表します。

関連：[HTML](../skills/foundation/html.basic.md)

### セマンティックHTML

見た目ではなく意味に沿って要素を選ぶHTMLの書き方です。見出しには見出し要素、ボタンにはボタン要素を使います。支援技術や検索エンジンが内容を正しく解釈できるようになります。

関連：[セマンティックHTML](../skills/applied-foundation/html.semantic.md)

### CSS

色、文字、余白、配置など、ページの見た目を指定する言語です。HTMLの要素に対してスタイルを当てます。

関連：[CSS](../skills/foundation/css.basic.md)

### セレクタ

CSSでスタイルを当てる対象を指定する記法です。要素名（`p`）、クラス（`.button`）、ID（`#main`）などで選びます。

関連：[CSS](../skills/foundation/css.basic.md)

### カスケードと詳細度

同じ要素に複数のスタイルが当たるとき、どれを優先するかを決める規則です。指定方法の具体性（詳細度）が高いもの、後に書かれたものが優先されます。表示が思いどおりにならない原因の多くはここにあります。

関連：[CSS](../skills/foundation/css.basic.md)

### ボックスモデル

各要素を、内容、内側の余白（padding）、枠線（border）、外側の余白（margin）の四層の箱として扱う考え方です。幅や高さの計算の基礎になります。

関連：[CSS](../skills/foundation/css.basic.md)

### FlexboxとGrid

CSSで要素を並べる仕組みです。Flexboxは横一列や縦一列といった一方向の配置に、Gridは行と列を持つ二次元の配置に向いています。

関連：[CSS](../skills/foundation/css.basic.md)

### レスポンシブデザイン

画面の幅や機器に応じて配置や文字の大きさを変え、スマートフォンからPCまで一つのHTMLで対応する設計です。

関連：[レスポンシブ設計](../skills/applied-foundation/css.responsive.md)

### JavaScript

ブラウザ上でページに動きを付けるプログラミング言語です。操作への反応、データの取得、画面の更新を担います。Node.jsを使うとサーバーや開発ツールでも動きます。

関連：[JavaScript](../skills/foundation/javascript.basic.md)

### DOM

Document Object Model。ブラウザがHTMLを読み込んで作る、要素の木構造です。JavaScriptはDOMを通じて要素を探し、内容や見た目を変更します。

関連：[DOM・イベント操作](../skills/applied-foundation/javascript.dom.md)

### イベント

クリック、文字入力、スクロール、読み込み完了など、ブラウザで起きる出来事です。JavaScriptはイベントに処理（ハンドラー）を登録して反応します。

関連：[DOM・イベント操作](../skills/applied-foundation/javascript.dom.md)

### 非同期処理

通信やタイマーのように時間のかかる処理を待つ間、他の処理を止めずに進める仕組みです。結果はPromiseやasync/awaitで受け取ります。

関連：[非同期処理](../skills/applied-foundation/javascript.async.md)

### Promise

非同期処理の「あとで届く結果」を表すオブジェクトです。成功か失敗のどちらかに落ち着き、`then` や `await` で結果を受け取ります。

関連：[非同期処理](../skills/applied-foundation/javascript.async.md)

### TypeScript

JavaScriptに型（値の種類の宣言）を加えた言語です。実行前に誤りを見つけやすく、エディタの補完が効きます。ビルド時にJavaScriptへ変換して動かします。

関連：[TypeScript](../skills/applied-foundation/typescript.basic.md)

### 型検査

変数や関数の値の種類が宣言と一致しているかを、実行前に機械的に確認することです。TypeScriptのコンパイラ（tsc）が行い、CIに組み込んで誤りの混入を防ぎます。

関連：[TypeScript](../skills/applied-foundation/typescript.basic.md)、[1-1 コードベース](../checklists/quality-and-types.md)

### フレームワークとライブラリ

ライブラリは特定の機能を提供する部品の集まりです。フレームワークは画面の構成方法や処理の流れまで含む土台です。ReactはUIを組み立てるライブラリ、Next.jsはReactを基にしたフレームワークです。

関連：[1-5 技術選定](../checklists/technology-selection.md)

### React

画面をコンポーネントという部品の組み合わせとして記述するUIライブラリです。データが変わると、画面の該当部分を自動で更新します。

関連：[React実装](../skills/implementation/react.basic.md)

### コンポーネント

見た目と動きをひとまとめにした、再利用できる画面の部品です。ボタン、入力欄、一覧などがあり、組み合わせて画面を作ります。

関連：[コンポーネント設計](../skills/implementation/react.component-design.md)、[1-3 UIコンポーネント](../checklists/ui-components.md)

### propsと状態

propsは親の部品から子の部品へ渡す設定値です。状態（state）は部品が持ち、操作や通信によって変わる値です。状態が変わると画面が再描画されます。

関連：[React実装](../skills/implementation/react.basic.md)

### 状態管理

画面の状態をどこに置き、どう更新・共有するかの設計です。部品の中だけで使う状態、複数の画面で共有する状態、URLに持たせる状態、サーバーから取得したデータを区別します。

関連：[状態管理](../skills/implementation/react.state-management.md)

### 楽観的更新

サーバーの応答を待たずに画面を先に更新し、失敗したら元に戻す手法です。操作の体感速度を上げます。

関連：[状態管理](../skills/implementation/react.state-management.md)

### フォーム

入力欄、選択肢、送信ボタンからなる、利用者が情報を入力する部分です。入力値の管理、検証、送信、エラー表示を扱います。

関連：[フォーム実装](../skills/implementation/react.form.md)

### 入力検証

入力値が必須項目を満たすか、形式や範囲が正しいかを確認することです。ブラウザ側で即時に確認して利用者に伝え、サーバー側でも必ず確認します。

関連：[入力検証・型連携](../skills/implementation/frontend.validation.md)

### スキーマ

データの形（項目名、型、必須かどうか）の定義です。Zodなどのライブラリで定義すると、実行時の検証と型定義の両方に使えます。

関連：[入力検証・型連携](../skills/implementation/frontend.validation.md)

### Storybook

コンポーネントを一つずつ表示・操作して確認できる開発ツールです。部品のカタログ、文書、テストの土台になります。

関連：[Storybook](../skills/implementation/storybook.basic.md)

### パッケージと依存関係

パッケージは公開されている再利用可能なコードの単位です。プロジェクトが利用するパッケージを依存関係と呼び、npmやpnpmなどのパッケージ管理ツールで導入・更新します。

関連：[3-4 サプライチェーン](../checklists/dependencies.md)

### ビルドとバンドル

開発時に書いたTypeScriptや多数のファイルを、ブラウザが読める形にまとめて変換する処理です。まとめた結果のファイルをバンドルと呼び、その大きさが表示速度に影響します。

関連：[3-2 ビルド](../checklists/builds.md)

### Lintと静的検査

コードを実行せずに、書き方の誤りや規約違反を機械的に見つけることです。ESLintやStylelintなどのツールを使います。字下げや改行を整えるにはPrettierなどのフォーマッタを使います。

関連：[JavaScript](../skills/foundation/javascript.basic.md)、[1-1 コードベース](../checklists/quality-and-types.md)

### 開発者ツール

ブラウザに内蔵された調査機能です。要素とスタイルの確認、通信の一覧、JavaScriptの実行とデバッグ、性能の計測ができます。多くのブラウザでF12キーから開けます。

関連：[Web基礎](../skills/foundation/web.basic.md)

### レイアウトとページ

App Routerでは、ディレクトリがURLに対応し、pageがその画面の内容、layoutが複数の画面で共有する枠（ヘッダーやナビゲーション）を表します。レイアウトは画面遷移をまたいで保持されます。

関連：[App Routerによる画面構成](../skills/implementation/nextjs.routing.md)

### Server ComponentsとClient Components

Server Componentsはサーバーで描画され、データベースやAPIへ直接アクセスできますが、クリックなどの操作は扱えません。Client Componentsはブラウザで動き、状態やイベントを扱います。App Routerでは両者を組み合わせて画面を作ります。

関連：[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)

### Server Actions

フォームの送信などをきっかけに、サーバー側の関数をブラウザから直接呼び出す仕組みです。APIの実装を省いてデータの更新を行え、更新後にキャッシュを再検証します。

関連：[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)

### ストリーミング

画面全体の準備を待たず、できた部分からブラウザへ順に送って表示する仕組みです。時間のかかる部分は読み込み中の表示を先に出し、後から差し替えます。

関連：[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)

### ハイドレーション

サーバーで描画したHTMLに、ブラウザでJavaScriptを結び付けて操作できる状態にする処理です。サーバーとブラウザで描画結果が食い違うと、警告や表示の乱れが起きます。

関連：[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)

### キャッシュの再検証

キャッシュした内容を、一定時間の経過やデータ更新をきっかけに取り直すことです。速さと鮮度の釣り合いを決める設定で、更新が画面に反映されない原因の多くはここにあります。

関連：[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)、[4-3 キャッシュ](../checklists/caching.md)

### ユーティリティクラス

余白、色、文字サイズなど一つの役割だけを持つ小さなクラスをHTMLに並べて見た目を指定する方法です。Tailwind CSSが代表で、クラス名の値はテーマから決まります。

関連：[スタイリング設計](../skills/implementation/frontend.styling.md)

### テーマとダークモード

テーマは、色や余白などの値をまとめて名前を付けたものです。ダークモードは、暗い背景向けの値の組に切り替える表示で、テーマの値を意味付け（背景、文字、強調など）で定義しておくと切り替えが容易になります。

関連：[スタイリング設計](../skills/implementation/frontend.styling.md)

## チーム開発の流れ

### リポジトリ

ソースコードと変更履歴を保管する場所です。GitHubやGitLabなどのサービス上で共有します。

関連：[Git](../skills/foundation/git.basic.md)

### Git

ファイルの変更履歴を記録し、複数人の並行作業を統合するためのバージョン管理システムです。

関連：[Git](../skills/foundation/git.basic.md)

### コミット

変更を履歴として記録する操作と、その記録の単位です。何を変えたかの説明（コミットメッセージ）を付けます。

関連：[Git](../skills/foundation/git.basic.md)

### ブランチ

履歴を分岐させ、本流に影響を与えずに作業する仕組みです。作業が終わったらマージで本流に戻します。

関連：[Git](../skills/foundation/git.basic.md)

### マージ

分岐したブランチの変更を別のブランチへ統合することです。同じ箇所を別々に変えていると衝突（コンフリクト）が起き、手作業で解消します。

関連：[Git](../skills/foundation/git.basic.md)

### Pull RequestとMerge Request

ブランチの変更を本流へ取り込んでほしいと依頼し、レビューと自動検査を受ける仕組みです。GitHubではPull Request（PR）、GitLabではMerge Request（MR）と呼びます。本書ではPRと表記し、GitLabではMRと読み替えます。

関連：[チーム開発](../skills/applied-foundation/git.collaboration.md)

### コードレビュー

他の開発者が変更内容を読み、誤り、設計、読みやすさを確認して指摘することです。PR上で行います。

関連：[チーム開発](../skills/applied-foundation/git.collaboration.md)

### CI

Continuous Integration（継続的インテグレーション）。変更がリポジトリに送られるたびに、ビルド、Lint、型検査、テストを自動で実行する仕組みです。GitHub ActionsやGitLab CI/CDで構成し、失敗した変更をマージできない設定にして品質を守ります。

関連：[3-5 CI/CD](../checklists/cicd.md)

### デプロイとCD

デプロイは、作成したアプリケーションを利用者が使えるサーバーや配信環境に配置することです。CD（継続的デリバリー）はそれを自動化し、いつでも安全に公開できる状態を保つことです。

関連：[3-3 デプロイ](../checklists/deployment.md)

### 環境

同じアプリケーションを動かす場所の区分です。開発者の手元（ローカル）、本番と同じ構成で確認するステージング、利用者が使う本番などがあります。

関連：[3-3 デプロイ](../checklists/deployment.md)

### Node.js

ブラウザの外でJavaScriptを動かす実行環境です。開発ツール、ビルド、テスト、サーバー処理に使います。

関連：[JavaScript](../skills/foundation/javascript.basic.md)

### フィーチャーフラグ

機能の有効・無効を設定で切り替える仕組みです。コードを公開したまま一部の利用者だけに機能を出したり、問題があれば即座に無効化したりできます。

関連：[3-3 デプロイ](../checklists/deployment.md)

### ロールバック

問題が起きたときに、以前の正常な版へ戻すことです。戻す手順を事前に用意し、試しておくことが重要です。

関連：[3-3 デプロイ](../checklists/deployment.md)

### Infrastructure as Code

サーバーや配信の設定をコードとして記述し、履歴管理と再現を可能にする手法です。手作業の設定変更による差異を防ぎます。

関連：[4-2 インフラ](../checklists/infrastructure.md)

## 品質・テスト

### 単体テスト

関数やモジュールなどの小さな単位を、単独で自動的に検証するテストです。速く実行でき、原因の特定が容易です。

関連：[単体テスト](../skills/quality/test.unit.md)

### コンポーネントテスト

画面の部品を描画し、利用者の操作を模して表示や動きを検証するテストです。

関連：[コンポーネントテスト](../skills/quality/test.component.md)

### 結合テスト

複数の部品や通信を組み合わせ、画面としての振る舞いを検証するテストです。APIはモックで置き換えることが多いです。

関連：[結合テスト](../skills/quality/test.integration.md)

### E2Eテスト

End to End。実際のブラウザを自動操作し、ログインから購入完了までのように、利用者の一連の操作が最後まで通ることを検証するテストです。

関連：[E2Eテスト](../skills/quality/test.e2e.md)

### テストピラミッド

速く安い単体テストを多く、遅く高いE2Eテストを少なくする、テストの配分の考え方です。

関連：[テスト設計](../skills/quality/test.design.md)

### モック

テストのために、通信先や外部の部品を偽物に置き換えることです。MSW（Mock Service Worker）はブラウザの通信を横取りしてモックするライブラリです。

関連：[結合テスト](../skills/quality/test.integration.md)

### カバレッジ

テストがコードのどの程度を実行したかの割合です。高いほど良いとは限らず、重要な経路が検証されているかを見ます。

関連：[単体テスト](../skills/quality/test.unit.md)

### 不安定なテスト

コードを変えていないのに、成功と失敗が変わるテストです。フレーキーとも呼びます。待ち時間や実行順序への依存が原因になりやすいです。

関連：[E2Eテスト](../skills/quality/test.e2e.md)

### ビジュアルリグレッションテスト

画面のスクリーンショットを以前のものと比較し、意図しない見た目の変化を検出するテストです。

関連：[Storybook](../skills/implementation/storybook.basic.md)

### アクセシビリティ

障害の有無や利用環境に関わらず、誰でも情報を得て操作できることです。キーボード操作、スクリーンリーダー対応、色のコントラストなどを含みます。a11yと略します。

関連：[アクセシビリティ](../skills/applied-foundation/web.accessibility.md)、[2-2 アクセシビリティ](../checklists/accessibility.md)

### WCAG

Web Content Accessibility Guidelines。アクセシビリティの国際的なガイドラインです。達成基準がA、AA、AAAの3段階で示されます。

関連：[アクセシビリティ](../skills/applied-foundation/web.accessibility.md)

### 支援技術とスクリーンリーダー

障害のある利用者がコンピューターを使うための道具です。スクリーンリーダーは画面の内容を音声で読み上げるソフトウェアで、HTMLの意味付けが正しくないと内容を伝えられません。

関連：[アクセシビリティ](../skills/applied-foundation/web.accessibility.md)

### Webパフォーマンス

ページの表示や操作への反応の速さです。通信量、JavaScriptの処理量、描画の仕方が影響します。

関連：[Webパフォーマンス](../skills/quality/web.performance.md)

### Core Web Vitals

Googleが定める利用者体験の指標です。表示の速さ（LCP）、操作への反応（INP）、表示のずれ（CLS）を測ります。

関連：[Webパフォーマンス](../skills/quality/web.performance.md)、[2-1 パフォーマンス](../checklists/performance.md)

### Lighthouse

Googleが提供する自動監査ツールです。性能、アクセシビリティ、SEOなどを採点します。ブラウザの開発者ツールからも実行できます。

関連：[Webパフォーマンス](../skills/quality/web.performance.md)

### SEO

Search Engine Optimization。検索エンジンに内容を正しく理解させ、検索結果に適切に表示されるようにすることです。見出しの構造、メタ情報、表示速度が関係します。

関連：[基本SEO](../skills/applied-foundation/web.seo.md)

## セキュリティ・運用・チーム

### 脆弱性

攻撃に悪用され得るソフトウェアの欠陥です。公開された既知の脆弱性にはCVEという識別番号が付きます。

関連：[Webセキュリティ](../skills/quality/web.security.md)

### XSS

Cross Site Scripting。攻撃者が用意したスクリプトを、他の利用者のブラウザで実行させる攻撃です。入力値をそのままHTMLに埋め込むと起きます。エスケープと検証で防ぎます。

関連：[Webセキュリティ](../skills/quality/web.security.md)

### CSP

Content Security Policy。ページが読み込めるスクリプトや通信先をサーバーが宣言し、不正なスクリプトの実行を防ぐ仕組みです。

関連：[Webセキュリティ](../skills/quality/web.security.md)

### SAST

Static Application Security Testing。コードを実行せずに、セキュリティ上の問題となる書き方を機械的に検出する検査です。

関連：[2-3 セキュリティ](../checklists/security.md)

### サプライチェーン

自分たちのコードが依存する外部パッケージ、ビルドツール、配信経路の全体です。依存先に脆弱性や悪意あるコードが混入するリスクを扱います。

関連：[3-4 サプライチェーン](../checklists/dependencies.md)

### 機密情報とシークレット管理

パスワード、APIキー、秘密鍵など、漏れると被害が出る情報（クレデンシャル）です。コードに書かず、専用の保管機構から実行時に渡します。

関連：[Webセキュリティ](../skills/quality/web.security.md)、[2-3 セキュリティ](../checklists/security.md)

### 依存関係の更新検知

DependabotやRenovateのように、依存パッケージの新版や脆弱性を検知して、更新のPRを自動で作る仕組みです。

関連：[3-4 サプライチェーン](../checklists/dependencies.md)

### プライバシーと外部送信

利用者の情報を扱うときの配慮です。分析や広告のために外部サービスへ利用者の情報を送ることを外部送信と呼び、日本では電気通信事業法に基づく通知・公表の規律があります。

関連：[2-4 プライバシー](../checklists/privacy.md)

### モニタリングとオブザーバビリティ

本番で動くシステムの状態を継続的に観測することです。ログ、メトリクス（数値）、トレース（処理の追跡）を集め、異常の検知と原因の調査に使います。

関連：[4-4 モニタリング](../checklists/observability.md)

### SLO

Service Level Objective。「表示は2秒以内が95%」のように、サービスの品質目標を数値で定めたものです。

関連：[4-4 モニタリング](../checklists/observability.md)

### インシデントとポストモーテム

インシデントは、利用者に影響する障害や問題です。ポストモーテムは、復旧後に経緯と原因を振り返り、個人を責めずに再発防止策を決める記録です。

関連：[4-5 障害対応](../checklists/incident-response.md)

### デザインシステムとデザイントークン

デザインシステムは、色、文字、部品、使い方の規則をまとめた共通の基盤です。デザイントークンは、色や余白などの値に名前を付けて、デザインツールとコードで共有する仕組みです。

関連：[2-5 デザイン](../checklists/design-consistency.md)

### DX Criteria

一般社団法人日本CTO協会が公開する、開発組織の状態を自己診断するための基準です。本書のチームチェックリストは、そのWebフロントエンド版を出典としています。

関連：[チームチェックリスト](../checklists/index.md)

### DORAの4指標

開発チームのデリバリー性能を測る4つの指標です。デプロイ頻度、変更のリードタイム、変更失敗率、復旧時間からなります。

関連：[5-1 専門性の育成](../checklists/knowledge-sharing.md)

### イネーブリング

他のチームが自力で課題を解決できるように、知識や仕組みを移して支援することです。代わりに作業するのではなく、できるようにすることを目指します。

関連：[5-2 イネーブリング](../checklists/engineering-improvement.md)

### ADR

Architecture Decision Record。設計上の判断を、背景、選択肢、決定、影響の形で記録した文書です。後から経緯を追えるようにします。

関連：[5-2 イネーブリング](../checklists/engineering-improvement.md)

<!-- glossary:end -->
