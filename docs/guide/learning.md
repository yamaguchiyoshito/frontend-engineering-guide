---
title: "学習コンテンツ"
description: "31の要素技術を学ぶ順路（まず読む資料とLv1の入口となる課題）と、無料で体系的に学べるコース、全体地図の一覧。学習の進め方と評価記録への結び付け方。"
---

# 学習コンテンツ

本書は評価の基準を示す文書であり、教材そのものは持ちません。このページは、何をどの順でどこで学ぶかの案内です。各要素技術ページに分かれている「はじめの一歩」と「まず読む」を一か所に集め、領域をまたいで通しで学べるコースと全体地図を添えています。

<!-- courses:start -->

無料で公開されている公式ドキュメント、公的機関の資料、実績のある教材から選んでいます。採用の推奨ではありません。2026年9月確認。

## 体系的なコース

領域をまたいで通しで学べる無料のコースです。日本語の資料を優先し、英語のみの資料には（英語）と付記しています。

### 基礎領域

- [MDN：Web開発を学ぶ](https://developer.mozilla.org/ja/docs/Learn_web_development) — Webの仕組みからHTML、CSS、JavaScriptまでを順に学ぶ入門コース。形式：手を動かす。対応：[Web基礎](../skills/foundation/web.basic.md)、[HTML](../skills/foundation/html.basic.md)、[CSS](../skills/foundation/css.basic.md)、[JavaScript](../skills/foundation/javascript.basic.md)
- [Chrome DevTools：ドキュメント](https://developer.chrome.com/docs/devtools?hl=ja) — 要素、通信、コンソール、性能の各パネルの使い方。形式：手を動かす。対応：[Web基礎](../skills/foundation/web.basic.md)、[DOM・イベント操作](../skills/applied-foundation/javascript.dom.md)
- [web.dev：Learn HTML](https://web.dev/learn/html?hl=ja) — HTMLの要素と意味付けの体系的なコース。形式：読む。対応：[HTML](../skills/foundation/html.basic.md)、[セマンティックHTML](../skills/applied-foundation/html.semantic.md)
- [web.dev：Learn CSS](https://web.dev/learn/css?hl=ja) — カスケード、ボックスモデル、レイアウトの体系的なコース。形式：読む。対応：[CSS](../skills/foundation/css.basic.md)
- [web.dev：Learn Forms](https://web.dev/learn/forms?hl=ja) — フォームの構造、検証、アクセシビリティのコース。形式：読む。対応：[HTML](../skills/foundation/html.basic.md)、[フォーム実装](../skills/implementation/react.form.md)
- [JavaScript Primer](https://jsprimer.net/) — ES2015以降の文法と非同期処理を、実行しながら学べる日本語の教科書。形式：手を動かす。対応：[JavaScript](../skills/foundation/javascript.basic.md)、[非同期処理](../skills/applied-foundation/javascript.async.md)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=ja_JP) — ブランチとマージをブラウザ上の演習で学ぶ。形式：手を動かす。対応：[Git](../skills/foundation/git.basic.md)
- [Pro Git（日本語版）](https://git-scm.com/book/ja/v2) — Gitの基本操作から内部構造までの解説書。形式：読む。対応：[Git](../skills/foundation/git.basic.md)、[チーム開発](../skills/applied-foundation/git.collaboration.md)

### 応用基礎領域

- [web.dev：Learn Responsive Design](https://web.dev/learn/design?hl=ja) — 画面幅と機器に応じた設計のコース。形式：読む。対応：[レスポンシブ設計](../skills/applied-foundation/css.responsive.md)
- [サバイバルTypeScript](https://typescriptbook.jp/) — 入門から実務の型の使い方までを扱う日本語の教科書。形式：読む。対応：[TypeScript](../skills/applied-foundation/typescript.basic.md)
- [GitHub Skills](https://skills.github.com/)（英語） — Pull Requestやレビューの流れを、練習用リポジトリで体験する。形式：手を動かす。対応：[チーム開発](../skills/applied-foundation/git.collaboration.md)
- [web.dev：Learn Accessibility](https://web.dev/learn/accessibility?hl=ja) — アクセシビリティの考え方と実装の体系的なコース。形式：読む。対応：[アクセシビリティ](../skills/applied-foundation/web.accessibility.md)、[セマンティックHTML](../skills/applied-foundation/html.semantic.md)
- [デジタル庁：ウェブアクセシビリティ導入ガイドブック](https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook) — 誰にとって何が障壁になるかから始める入門書。形式：読む。対応：[アクセシビリティ](../skills/applied-foundation/web.accessibility.md)
- [Google検索セントラル：SEOスターターガイド](https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=ja) — 検索エンジンにページを理解させる基本。形式：読む。対応：[基本SEO](../skills/applied-foundation/web.seo.md)

### フレームワーク・実装領域

- [React：チュートリアル（三目並べ）](https://ja.react.dev/learn/tutorial-tic-tac-toe) — コンポーネント、props、stateを一つのゲームを作りながら学ぶ。形式：手を動かす。対応：[React実装](../skills/implementation/react.basic.md)、[状態管理](../skills/implementation/react.state-management.md)
- [Next.js：Learn](https://nextjs.org/learn)（英語） — App Routerでダッシュボードを作りながら、ルーティング、データ取得、認証までを学ぶ公式コース。形式：手を動かす。対応：[App Routerによる画面構成](../skills/implementation/nextjs.routing.md)、[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)
- [Tailwind CSS：Styling with utility classes](https://tailwindcss.com/docs/styling-with-utility-classes)（英語） — ユーティリティクラスの考え方とテーマの扱い。形式：読む。対応：[スタイリング設計](../skills/implementation/frontend.styling.md)
- [Storybook：チュートリアル](https://storybook.js.org/tutorials/)（英語） — 部品のカタログ化からテストまでを段階的に学ぶ公式チュートリアル。形式：手を動かす。対応：[Storybook](../skills/implementation/storybook.basic.md)、[コンポーネント設計](../skills/implementation/react.component-design.md)

### 品質・高度化領域

- [Vitest：ガイド](https://vitest.dev/guide/)（英語） — 導入と最初のテストの書き方。形式：手を動かす。対応：[単体テスト](../skills/quality/test.unit.md)
- [Testing Library：ドキュメント](https://testing-library.com/docs/)（英語） — 利用者の見え方で要素を取得するテストの考え方と書き方。形式：読む。対応：[コンポーネントテスト](../skills/quality/test.component.md)
- [Mock Service Worker：ドキュメント](https://mswjs.io/docs/)（英語） — 通信をモックしてテストする仕組みと手順。形式：手を動かす。対応：[結合テスト](../skills/quality/test.integration.md)
- [Playwright：Getting started](https://playwright.dev/docs/intro)（英語） — 導入、操作の記録、実行までの公式ガイド。形式：手を動かす。対応：[E2Eテスト](../skills/quality/test.e2e.md)
- [web.dev：Learn Performance](https://web.dev/learn/performance?hl=ja) — 計測から画像、フォント、コード分割までの体系的なコース。形式：読む。対応：[Webパフォーマンス](../skills/quality/web.performance.md)
- [IPA：安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity.html) — 代表的な脆弱性の仕組みと対策を日本語で解説。形式：読む。対応：[Webセキュリティ](../skills/quality/web.security.md)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)（英語） — 対策の実装指針を分野別にまとめた資料。形式：読む。対応：[Webセキュリティ](../skills/quality/web.security.md)、[入力検証・型連携](../skills/implementation/frontend.validation.md)

## 全体地図

学習項目の全体像を見渡すための外部の地図です。分類は本書の要素技術と一致しないため、対応する領域や要素技術を付記しています。

- [roadmap.sh：Frontend Developer](https://roadmap.sh/frontend)（英語） — フロントエンド全体の学習項目の地図。本書の基礎領域と応用基礎領域に相当
- [roadmap.sh：React](https://roadmap.sh/react)（英語） — Reactとその周辺ライブラリの地図。本書のフレームワーク・実装領域に相当
- [roadmap.sh：Next.js](https://roadmap.sh/nextjs)（英語） — Next.jsの地図。本書の「App Routerによる画面構成」「レンダリングとデータ取得」に相当
- [roadmap.sh：Frontend Performance Best Practices](https://roadmap.sh/frontend-performance-best-practices)（英語） — 性能改善の項目一覧。本書の「Webパフォーマンス」に相当

<!-- courses:end -->

## 学習の順路

要素技術は、基礎領域、応用基礎領域、フレームワーク・実装領域、品質・高度化領域の順に積み重なります。各要素技術について、最初に読む資料と、Lv1の入口となる課題を示します。課題を自分で実行できたら、作ったものを根拠にして[個人の習熟度評価記録](../templates/individual-assessment.md)に自己評価を書きます。すべてを順番に学ぶ必要はなく、担当業務で必要な要素技術と、その「主な前提」から選んでください。

<!-- route:start -->

### 基礎領域

1. **[Web基礎](../skills/foundation/web.basic.md)**（評価対象：HTTP、URL、ブラウザ、Cookie、キャッシュ）  
   まず読む：[MDN：Webの仕組み](https://developer.mozilla.org/ja/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)  
   Lv1の入口となる課題：MDNの「Webの仕組み」で、ブラウザがサーバーへ要求を送り、応答を受け取る流れを読みます。次に、開発者ツールのNetworkパネルで任意のページを開いたときの要求一覧、ステータスコード、応答ヘッダーを自分で確認できれば、Lv1の入口です。
2. **[HTML](../skills/foundation/html.basic.md)**（評価対象：文書構造、フォーム、基本要素）  
   まず読む：[MDN：HTMLの学習](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Structuring_content)  
   Lv1の入口となる課題：MDNの「HTMLの学習」に沿って、見出し、段落、リンク、画像、リストだけの短いページを一つ作り、ブラウザで表示します。フォームの入力欄と送信ボタンまで置き、W3Cの検証サービスで指摘された誤りを直せれば、Lv1の入口です。
3. **[CSS](../skills/foundation/css.basic.md)**（評価対象：セレクタ、ボックスモデル、レイアウト）  
   まず読む：[MDN：CSSの学習](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Styling_basics)  
   Lv1の入口となる課題：MDNの「CSSの学習」で、色、文字、余白の指定から始め、ボックスモデルとFlexboxまでを手を動かして確認します。開発者ツールで要素に当たっているスタイルを見て、自分の変更がどう反映されたかを説明できれば、Lv1の入口です。
4. **[JavaScript](../skills/foundation/javascript.basic.md)**（評価対象：構文、関数、オブジェクト、配列）  
   まず読む：[JavaScript Primer](https://jsprimer.net/)  
   Lv1の入口となる課題：「JavaScript Primer」の基本文法（変数、関数、配列、オブジェクト）を、ブラウザの開発者ツールのコンソールで実行しながら読みます。短い関数を自分で書いて結果を確認し、エラーメッセージを読んで直せれば、Lv1の入口です。
5. **[Git](../skills/foundation/git.basic.md)**（評価対象：branch、commit、merge、rebase）  
   まず読む：[Pro Git（日本語版）](https://git-scm.com/book/ja/v2)  
   Lv1の入口となる課題：「Pro Git」の1章と2章に沿って、リポジトリの作成、変更の記録（commit）、履歴の確認までを実際に操作します。ブランチを一つ作って変更し、元のブランチへマージできれば、Lv1の入口です。

### 応用基礎領域

1. **[セマンティックHTML](../skills/applied-foundation/html.semantic.md)**（主な前提：HTML）  
   まず読む：[MDN：HTML要素リファレンス](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements)  
   Lv1の入口となる課題：MDNの「HTML要素リファレンス」で、header、nav、main、article、section、footerなど意味を表す要素を確認し、自分のページの各領域に当てはめます。開発者ツールのアクセシビリティツリーで、見出しの階層と領域が意図どおりに読まれることを確認できれば、Lv1の入口です。
2. **[レスポンシブ設計](../skills/applied-foundation/css.responsive.md)**（主な前提：CSS）  
   まず読む：[MDN：レスポンシブデザイン](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)  
   Lv1の入口となる課題：MDNの「レスポンシブデザイン」で、メディアクエリと相対的な単位の使い方を読みます。開発者ツールのデバイスモードで幅を変え、一つの画面がスマートフォンの幅とPCの幅で崩れずに並び替わる状態を作れれば、Lv1の入口です。
3. **[DOM・イベント操作](../skills/applied-foundation/javascript.dom.md)**（主な前提：JavaScript）  
   まず読む：[MDN：イベント入門](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Scripting/Events)  
   Lv1の入口となる課題：MDNの「イベント入門」で、要素の取得、内容の書き換え、クリックへの反応を試します。ボタンを押すと文字が変わる小さなページを作り、開発者ツールで登録したイベントリスナーを確認できれば、Lv1の入口です。
4. **[非同期処理](../skills/applied-foundation/javascript.async.md)**（主な前提：JavaScript）  
   まず読む：[JavaScript Primer：非同期処理](https://jsprimer.net/basic/async/)  
   Lv1の入口となる課題：「JavaScript Primer」の非同期処理の章で、Promiseとasync/awaitがなぜ必要かと、その書き方を読みます。fetchで公開APIからデータを取得し、成功したときと失敗したときの表示を分けられれば、Lv1の入口です。
5. **[TypeScript](../skills/applied-foundation/typescript.basic.md)**（主な前提：JavaScript）  
   まず読む：[サバイバルTypeScript](https://typescriptbook.jp/)  
   Lv1の入口となる課題：「サバイバルTypeScript」の入門で、基本の型、関数の型、オブジェクトの型を読みます。既存のJavaScriptの短い関数に型を付け、tscが出す型エラーを読んで直せれば、Lv1の入口です。
6. **[アクセシビリティ](../skills/applied-foundation/web.accessibility.md)**（主な前提：HTML、セマンティックHTML）  
   まず読む：[デジタル庁：ウェブアクセシビリティ導入ガイドブック](https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook)  
   Lv1の入口となる課題：デジタル庁の「ウェブアクセシビリティ導入ガイドブック」で、誰にとって何が障壁になるのかを読みます。自分の画面をキーボードだけで操作し、画像の代替テキストと見出しの構造を確認して、Lighthouseの指摘を一つ直せれば、Lv1の入口です。
7. **[基本SEO](../skills/applied-foundation/web.seo.md)**（主な前提：HTML、セマンティックHTML）  
   まず読む：[Google検索セントラル](https://developers.google.com/search/docs?hl=ja)  
   Lv1の入口となる課題：「Google検索セントラル」のSEOスターターガイドで、検索エンジンがページを見つけて理解する仕組みを読みます。title、説明文（meta description）、見出しを整え、LighthouseのSEO監査を通せれば、Lv1の入口です。
8. **[チーム開発](../skills/applied-foundation/git.collaboration.md)**（主な前提：Git）  
   まず読む：[GitHub Docs：Pull Request](https://docs.github.com/ja/pull-requests)  
   Lv1の入口となる課題：GitHub Docsの「Pull Request」で、ブランチで変更を提案し、レビューを受けてマージするまでの流れを読みます。練習用のリポジトリで自分のPRを一つ作り、指摘を受けて修正を追加のコミットとして積めれば、Lv1の入口です。

### フレームワーク・実装領域

1. **[React実装](../skills/implementation/react.basic.md)**（主な前提：JavaScript、TypeScript、DOM）  
   まず読む：[React：学習（日本語）](https://ja.react.dev/learn)  
   Lv1の入口となる課題：React公式の「学習」のクイックスタートで、コンポーネント、JSX、propsとstateを順に試します。ボタンを押すと数が増えるコンポーネントを自分で書き、stateが変わると画面が更新される理由を説明できれば、Lv1の入口です。
2. **[コンポーネント設計](../skills/implementation/react.component-design.md)**（主な前提：React、UI実装）  
   まず読む：[React：Reactの流儀（日本語）](https://ja.react.dev/learn/thinking-in-react)  
   Lv1の入口となる課題：「Reactの流儀」で、画面をコンポーネントに分け、stateをどこに置くかを決める手順を読みます。既存の画面を三つ程度の部品に分割し、親から子へpropsを渡す形に書き直せれば、Lv1の入口です。
3. **[状態管理](../skills/implementation/react.state-management.md)**（主な前提：React、非同期処理）  
   まず読む：[React：stateの管理（日本語）](https://ja.react.dev/learn/managing-state)  
   Lv1の入口となる課題：React公式の「stateの管理」で、stateの構造の選び方と、親コンポーネントへのリフトアップを読みます。二つのコンポーネントで共有する値を親に持ち上げ、両方の表示を同期できれば、Lv1の入口です。
4. **[フォーム実装](../skills/implementation/react.form.md)**（主な前提：React、TypeScript）  
   まず読む：[React：form要素（日本語）](https://ja.react.dev/reference/react-dom/components/form)  
   Lv1の入口となる課題：React公式のform要素の解説で、入力値の取得と送信の流れを読みます。名前とメールアドレスの二項目のフォームを作り、必須チェックのエラーを表示してから送信できれば、Lv1の入口です。
5. **[REST API連携](../skills/implementation/frontend.api-integration.md)**（主な前提：非同期処理、TypeScript）  
   まず読む：[MDN：Fetch API](https://developer.mozilla.org/ja/docs/Web/API/Fetch_API)  
   Lv1の入口となる課題：MDNの「Fetch API」で、要求の送り方と応答の読み方を確認します。公開APIから一覧を取得して画面に表示し、読み込み中とエラーの表示を分けられれば、Lv1の入口です。
6. **[入力検証・型連携](../skills/implementation/frontend.validation.md)**（主な前提：フォーム、TypeScript）  
   まず読む：[Zod](https://zod.dev/)  
   Lv1の入口となる課題：Zodの公式ドキュメントで、スキーマの定義と検証の書き方を読みます。フォームの入力値をスキーマで検証し、エラーメッセージを項目ごとに表示できれば、Lv1の入口です。
7. **[Storybook](../skills/implementation/storybook.basic.md)**（主な前提：React、コンポーネント設計）  
   まず読む：[Storybook：ドキュメント](https://storybook.js.org/docs)  
   Lv1の入口となる課題：Storybook公式ドキュメントの「Get started」で、導入と最初のStoryの書き方を読みます。既存のボタンなど一つの部品について、通常・無効・読み込み中の状態を別々のStoryとして表示できれば、Lv1の入口です。
8. **[App Routerによる画面構成](../skills/implementation/nextjs.routing.md)**（主な前提：React実装、Web基礎）  
   まず読む：[Next.js：Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)  
   Lv1の入口となる課題：Next.js公式の「Layouts and Pages」で、ディレクトリ構成がそのままURLになる仕組みと、レイアウトが画面をまたいで維持される理由を読みます。一覧と詳細の2画面を、共通レイアウトと動的ルートで作り、リンクで行き来できれば、Lv1の入口です。
9. **[レンダリングとデータ取得](../skills/implementation/nextjs.rendering.md)**（主な前提：App Routerによる画面構成、REST API連携、非同期処理）  
   まず読む：[Next.js：Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)  
   Lv1の入口となる課題：Next.js公式の「Server and Client Components」で、どちらの部品がどこで動き、何ができて何ができないかを読みます。一覧画面をServer Componentでデータ取得して描画し、並べ替えなど操作が必要な部分だけをClient Componentに切り出せれば、Lv1の入口です。
10. **[スタイリング設計](../skills/implementation/frontend.styling.md)**（主な前提：CSS、レスポンシブ設計、コンポーネント設計）  
   まず読む：[Tailwind CSS：Styling with utility classes](https://tailwindcss.com/docs/styling-with-utility-classes)  
   Lv1の入口となる課題：Tailwind CSS公式の「Styling with utility classes」で、クラスを組み合わせて見た目を指定する考え方と、テーマの値がどこで決まるかを読みます。既存のボタンについて、通常・強調・無効の3種類をテーマの色だけで表現し、画面幅に応じて余白を変えられれば、Lv1の入口です。

### 品質・高度化領域

1. **[単体テスト](../skills/quality/test.unit.md)**（主な前提：JavaScript、TypeScript）  
   まず読む：[Vitest：ガイド](https://vitest.dev/guide/)  
   Lv1の入口となる課題：Vitestの「Getting Started」で、テストファイルの置き方とexpectの書き方を読みます。純粋な関数を一つ選び、通常の入力と境界の入力のテストを書いて実行できれば、Lv1の入口です。
2. **[コンポーネントテスト](../skills/quality/test.component.md)**（主な前提：React）  
   まず読む：[React Testing Library：入門](https://testing-library.com/docs/react-testing-library/intro/)  
   Lv1の入口となる課題：React Testing Libraryの入門で、利用者の見え方で要素を取得する考え方を読みます。ボタンを押すと表示が変わる部品について、操作と結果の確認をテストとして書ければ、Lv1の入口です。
3. **[結合テスト](../skills/quality/test.integration.md)**（主な前提：React、API連携）  
   まず読む：[Mock Service Worker：ドキュメント](https://mswjs.io/docs/)  
   Lv1の入口となる課題：MSWの「Getting started」で、通信を偽の応答に置き換える仕組みを読みます。一覧画面のテストで、APIの成功応答と失敗応答をモックし、それぞれの表示を確認できれば、Lv1の入口です。
4. **[E2Eテスト](../skills/quality/test.e2e.md)**（主な前提：フォーム、API連携）  
   まず読む：[Playwright：ドキュメント](https://playwright.dev/docs/intro)  
   Lv1の入口となる課題：Playwrightの「Getting started」で、導入、操作の記録、実行の流れを読みます。ログインして一覧が表示されるまでのシナリオを一つ書き、手元とCIの両方で実行できれば、Lv1の入口です。
5. **[テスト設計](../skills/quality/test.design.md)**（主な前提：各テスト実装）  
   まず読む：[Martin Fowler：The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)  
   Lv1の入口となる課題：Martin Fowlerの「The Practical Test Pyramid」で、テストの種類ごとの役割と配分を読みます。一つの機能について、何を単体テスト、コンポーネントテスト、E2Eテストのどこで確認するかを表に書き分けられれば、Lv1の入口です。
6. **[Webパフォーマンス](../skills/quality/web.performance.md)**（主な前提：HTML、CSS、JavaScript、React）  
   まず読む：[web.dev：Core Web Vitals](https://web.dev/articles/vitals?hl=ja)  
   Lv1の入口となる課題：web.devの「Core Web Vitals」で、LCP、INP、CLSがそれぞれ何を測るかを読みます。自分の画面をLighthouseで計測し、指摘された項目の意味を説明して一つ改善できれば、Lv1の入口です。
7. **[Webセキュリティ](../skills/quality/web.security.md)**（主な前提：Web基礎、JavaScript、API連携）  
   まず読む：[IPA：安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity.html)  
   Lv1の入口となる課題：IPAの「安全なウェブサイトの作り方」で、XSSなど代表的な脆弱性の仕組みと対策を読みます。自分の画面で利用者の入力をそのままHTMLに出している箇所を探し、エスケープや検証で直せれば、Lv1の入口です。
8. **[フロントエンド品質保証](../skills/quality/frontend.quality.md)**（主な前提：テスト設計、性能、セキュリティ）  
   まず読む：[Webフロントエンド版DX Criteria](https://dxcriteria.cto-a.org/frontend)  
   Lv1の入口となる課題：「Webフロントエンド版DX Criteria」のテストとCI/CDの項目で、チームとして何を自動化すべきかを読みます。自分のリポジトリでLint、型検査、テストをCIで実行し、失敗した変更をマージできない設定を確認できれば、Lv1の入口です。

<!-- route:end -->

## 学習の進め方と記録

1. [初めて自己評価する方へ](individual-assessment.md#初めて自己評価する方へ)の4つの原則に従います。基礎領域の5つから始め、用語が分からない要素技術は未評価にし、課題を試してから再評価し、根拠は作ったもので残します。
2. 学習の目標は、[個人の習熟度評価記録](../templates/individual-assessment.md)の「次の到達条件」に書きます。読む資料の量ではなく、どの課題を実行できる状態を目指すかを書きます。
3. 課題を終えたら、作成したページ、コード、リポジトリの履歴を「根拠」に記入し、評価者と確認します。[記入例：Gitの習熟度を初めて評価する](../examples/git-first-assessment.md)に、未評価から始めてLv1と判定されるまでの流れがあります。
4. 分からない用語は[用語集](glossary.md)で確認し、載っていない用語は[MDNの用語集](https://developer.mozilla.org/ja/docs/Glossary)で確認します。

教材の追加や差し替えは、[編集・検証・公開手順](../maintenance/contributing.md)に沿って `build/learning.json` を更新してください。到達確認は参考リンクと同じ週次のワークフローで行います。
