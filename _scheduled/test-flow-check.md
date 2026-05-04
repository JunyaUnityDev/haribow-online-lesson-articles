---
layout: article
title: "【動作確認テスト】Phase 3-B 全フロー再点検"
description: "公開→GAS通知→LINE配信の一連を再確認するためのテスト記事"
date: 2026-01-01
publish_date: 2026-05-04
category: culture
slug: test-flow-check
order: 999
---

これは Phase 3-B（記事自動公開 + LINE 配信）の全フロー動作確認用のテスト記事です。

このメッセージが JUNYA の LINE に届けば、以下が成功:

1. cron / workflow_dispatch で `Scheduled Article Publish` 起動
2. `publish_date <= JST今日` の検出
3. `_scheduled/test-flow-check.md` → `_posts/2026-05-04-test-flow-check.md` リネーム
4. auto-commit + push
5. workflow_run で Jekyll build 自動起動
6. future:true でビルド対象に含まれる
7. GAS Web App に HTTP POST（共有秘密で認証）
8. ArticlePublishHandler が `slug.startsWith('test-')` を検出 → テストモード
9. `config.testRecipientUserId` (JUNYA) のみに LINE push
10. 受講生全員には届かない

テスト後すぐに削除します。
