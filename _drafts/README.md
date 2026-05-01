# _drafts/ ディレクトリ

このディレクトリは Jekyll の **下書き記事** を置く場所。

ここに置いた md ファイルは:

- 通常のビルドでは **公開されない**(GitHub Pages 上には出ない)
- ローカルで `bundle exec jekyll serve --drafts` するとプレビューできる
- 公開する時は `_posts/YYYY-MM-DD-slug.md` にリネーム移動

## ファイル名

- `_drafts/` 内では日付プレフィックス不要
- 例: `_drafts/new-article-idea.md`

## Front Matter

通常の記事と同じ Front Matter を書く:

```yaml
---
layout: article
title: "記事タイトル"
description: "概要(2行程度)"
date: 2026-06-01    # 想定公開日(参考用、_posts に移動時にファイル名と一致させる)
category: mindset    # mindset または technique
slug: new-article    # URL用
---
```

## 公開フロー

1. `_drafts/new-article.md` を完成させる
2. `_posts/2026-06-01-new-article.md` にリネーム移動
3. git push → GitHub Actions が自動でビルド & 公開
4. USER_BOOK スプシの「記事ストック」シートでステータスを「公開済み」に更新

## ストック残数の確認

USER_BOOK スプシの「記事ストック」シートで:

- ステータス「ネタ」+「執筆中」+「完成」の件数 = ストック残数
- Phase 3-B で残数監視 + 通知システムを実装予定
