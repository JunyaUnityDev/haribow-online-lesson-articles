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
├── _posts/                  ← 公開記事 md（YYYY-MM-DD-slug.md）
├── _drafts/                 ← 下書き記事（公開されない、ローカルプレビューのみ）
├── assets/                  ← {css,images}
├── articles/index.html      ← 記事一覧
├── category/                ← {mindset,technique}/index.html
├── about/index.html         ← About ページ
├── .github/workflows/jekyll.yml ← Actions ビルド
├── .template/               ← 記事制作指示書テンプレート（ビルド対象外）
├── Gemfile
├── index.html               ← トップ
├── README.md
└── .gitignore
```

## 記事制作フロー

### ストック管理

USER_BOOK スプシの「記事ストック」シート（`SHEET_NAME.ARTICLE_STOCK`）で全記事のネタ・進捗を管理。

- 列: タイトル候補 / カテゴリ / ステータス / 想定公開日 / スラッグ / ファイルパス / 概要 / メモ / 公開URL
- ステータス: ネタ → 執筆中 → 完成 → 公開済み

### 記事を新規制作する流れ

1. JUNYA がネタを思いつく
2. USER_BOOK の「記事ストック」シートに行追加（タイトル候補・カテゴリ・メモ、ステータス「ネタ」）
3. JUNYA が ChatClaude に「この記事書きたい」と相談
4. ChatClaude が構成案を提示 → JUNYA とミーティング（読者層・結論・構成・文体・参考資料）
5. ChatClaude が `.template/ARTICLE_REQUEST_TEMPLATE.md` を埋めた記事制作指示書を作成
6. JUNYA が Claude Code に指示書を投げる
7. Claude Code が `_drafts/{slug}.md` を作成（ステータス「執筆中」）
8. JUNYA が確認・微調整（ステータス「完成」）
9. 公開時: `_posts/YYYY-MM-DD-{slug}.md` にリネーム移動
   - ステータス「公開済み」、公開URL を記入

### 動画・画像・音源の埋め込み

- 画像: `![alt]({{ '/assets/images/file.jpg' | relative_url }})`
- YouTube: `<div class="video-embed"><iframe src="https://www.youtube.com/embed/VIDEO_ID" ...></iframe></div>`
- note 音源: `<div class="sound-embed"><iframe src="https://note.com/embed/sounds/SOUND_ID" height="275" ...></iframe></div>`
- 各クラスは `assets/css/main.scss` の `.article-body` 内に定義済み

### Phase 3-B（将来）

- 予約投稿システム: USER_BOOK の想定公開日を見て自動的に `_posts/` に移動 + push
- LINE 一斉配信: 公開時に受講者へ概要 + URL を配信
- ストック残数監視: 残数が少なくなったら JUNYA に通知

### よく使うコマンド

```bash
# ローカルで下書き含めてプレビュー（要 Jekyll セットアップ）
bundle exec jekyll serve --drafts

# 通常プレビュー（公開済みのみ）
bundle exec jekyll serve

# push（GitHub Actions が自動ビルド・公開）
git add . && git commit -m "Add article: xxx" && git push
```

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
