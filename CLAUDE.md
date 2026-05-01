# HARIBOW Online Lesson - Articles サイト

## 概要

HARIBOW のオンラインレッスン受講者向け記事サイト。
GitHub Pages + Jekyll + GitHub Actions ビルド。

## 公開URL

https://junyaunitydev.github.io/haribow-online-lesson-articles/

## ディレクトリ構造

```
haribow-online-lesson-articles/
├── _config.yml              ← Jekyll 設定
├── _data/categories.yml     ← カテゴリ定義
├── _layouts/                ← {default,home,article,category}.html
├── _includes/               ← {header,footer,article-card}.html
├── _posts/                  ← 記事 md（YYYY-MM-DD-slug.md）
├── assets/css/main.scss     ← スタイル
├── articles/index.html      ← 記事一覧
├── category/                ← {mindset,technique}/index.html
├── about/index.html         ← About ページ
├── .github/workflows/jekyll.yml ← Actions ビルド
├── Gemfile
├── index.html               ← トップ
├── README.md
└── .gitignore
```

## 記事追加フロー

1. `_posts/YYYY-MM-DD-slug.md` を作成
2. Front Matter に必要なメタデータを記入
   ```yaml
   ---
   layout: article
   title: "記事タイトル"
   description: "短い説明"
   date: YYYY-MM-DD
   category: mindset|technique
   slug: my-article-slug
   order: N
   ---
   ```
3. git push → GitHub Actions が自動でビルド & 公開（1〜3分）

## カテゴリ

- mindset: 思想 / 継続の科学
- technique: 技術 / ソロ研究

カテゴリ追加時は `_data/categories.yml` を更新。

## 関連プロジェクト

- `/Users/apple/projects/haribow/online_lesson/`（GAS自動化、配信システム連携予定）
- 記事公開時の LINE 一斉配信は Phase 3-B で実装予定

## 現状

- Phase 3-A 完了: 既存4記事公開
- Phase 3-B 未着手: 予約投稿システム + LINE配信

## 注意

- 記事内のスプレッドシート誘導は LINE「練習」運用に書き換え済み
- 動画/画像参照箇所は「後日追加予定」プレースホルダー
- ChatClaude が生成した記事本文は改変禁止（Claude Code 側からは編集しない）
