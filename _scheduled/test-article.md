---
layout: article
title: "【統合テスト】Phase 3-B 動作確認用"
description: "GitHub Actions cron + Python スクリプト + GAS LINE 配信の一連を確認するためのテスト記事"
date: 2026-01-01
publish_date: 2026-05-04
category: culture
slug: test-article
order: 999
---

これは Phase 3-B の統合テスト用の記事です。

このメッセージが LINE で JUNYA に届けば、以下のフロー全部が成功している:

1. workflow_dispatch で `Scheduled Article Publish` workflow が起動
2. `_scheduled/test-article.md` を読み、`publish_date: 2026-05-04` <= 今日 を判定
3. `_posts/2026-05-04-test-article.md` にリネーム + commit + push
4. GAS Web App に HTTP POST で通知（共有秘密で認証）
5. ArticlePublishHandler が slug が `test-` で始まることを検出 → テストモード
6. JUNYA の userId に LINE で push（受講生全員には届かない）

テスト後、このファイルは削除されます。
