# _scheduled/ ディレクトリ

このディレクトリは Jekyll の **予約公開記事** を置く場所。

ここに置いた md ファイルは:
- `/scheduled/{slug}/` の URL で **公開される**（隠しページ、サイト内導線なし）
- `/scheduled/` 一覧ページで運営が確認できる（URL 直打ち専用）
- `publish_date` の日付になると、GitHub Actions cron が自動的に `_posts/` に移動 → 通常公開

## ファイル名

- `_scheduled/` 内では日付プレフィックス不要
- 例: `_scheduled/new-article.md`

## Front Matter

```yaml
---
layout: article
title: "記事タイトル"
description: "概要(2行程度、LINE配信用)"
date: 2026-05-01            # 仮の日付（cron が publish_date に書き換える）
publish_date: 2026-06-15    # ★ 実際の公開予定日（必須）
category: culture
slug: new-article
order: 6
line_message: |              # ★ LINE配信文言カスタマイズ（任意）
  📝 新しい記事を公開しました!

  『{title}』
  {description}

  → {url}
---
```

## 公開フロー（自動）

毎月15日 09:00 JST に GitHub Actions cron が起動:

1. `_scheduled/*.md` を走査
2. `publish_date <= today` の記事を検出
3. `_scheduled/{slug}.md` → `_posts/{publish_date}-{slug}.md` にリネーム
4. front matter の `date` を `publish_date` に書き換え、`publish_date` フィールド削除
5. git commit + push
6. GitHub Actions 既存の jekyll build が動いて公開
7. GAS Web App に HTTP POST で通知
8. GAS が LINE Multicast で受講生に配信

## 公開フロー（手動、緊急時のみ）

1. `_scheduled/{slug}.md` を `_posts/YYYY-MM-DD-{slug}.md` にリネーム
2. front matter の `date` を公開日に修正、`publish_date` を削除
3. git push

## ストック残数の確認

- `/scheduled/` 一覧ページ（本番URL）で全件ブラウザ確認
- USER_BOOK スプシの「記事ストック」シートで管理
