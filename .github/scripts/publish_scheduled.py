#!/usr/bin/env python3
"""
_scheduled/ 配下の md ファイルを走査し、
publish_date <= today のものを _posts/{publish_date}-{slug}.md にリネーム。
リネーム後、GAS Web App に通知 HTTP POST を送信。

環境変数:
  GAS_WEBHOOK_URL          - GAS Web App URL（LINE配信エンドポイント）
  ARTICLE_PUBLISH_SECRET   - 共有秘密（GAS PropertiesService と一致）
  SITE_BASE_URL            - サイトのベースURL（末尾スラッシュなし）
"""

import os
import sys
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

import yaml
import requests

# 日本標準時（JST）。GitHub Actions runner は UTC で動くため、
# 日付比較は JST に揃える。本番 cron (毎月15日 00:00 UTC = 09:00 JST) でも
# JST の同日扱いになる。
JST = timezone(timedelta(hours=9))


SCHEDULED_DIR = Path('_scheduled')
POSTS_DIR = Path('_posts')

GAS_WEBHOOK_URL = os.environ.get('GAS_WEBHOOK_URL', '')
ARTICLE_PUBLISH_SECRET = os.environ.get('ARTICLE_PUBLISH_SECRET', '')
SITE_BASE_URL = os.environ.get(
    'SITE_BASE_URL',
    'https://junyaunitydev.github.io/haribow-online-lesson-articles'
)


def parse_front_matter(content):
    """md ファイルから front matter と本文を抽出。"""
    if not content.startswith('---\n'):
        return None, content

    end_idx = content.find('\n---\n', 4)
    if end_idx == -1:
        return None, content

    fm_text = content[4:end_idx]
    body = content[end_idx + 5:]

    try:
        fm = yaml.safe_load(fm_text)
        return fm, body
    except yaml.YAMLError as e:
        print(f"YAML parse error: {e}", file=sys.stderr)
        return None, content


def serialize_front_matter(fm, body):
    """front matter を md 形式にシリアライズ。"""
    fm_text = yaml.dump(
        fm,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )
    return f"---\n{fm_text}---\n{body}"


def main():
    today = datetime.now(JST).date()
    print(f"[publish_scheduled] Today (JST): {today}")

    if not SCHEDULED_DIR.exists():
        print(f"[publish_scheduled] {SCHEDULED_DIR} does not exist, skipping")
        set_output('published_count', 0)
        return

    POSTS_DIR.mkdir(exist_ok=True)

    published = []

    for md_file in sorted(SCHEDULED_DIR.glob('*.md')):
        if md_file.name == 'README.md':
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"[publish_scheduled] Failed to read {md_file}: {e}", file=sys.stderr)
            continue

        fm, body = parse_front_matter(content)
        if fm is None:
            print(f"[publish_scheduled] No front matter in {md_file}, skipping", file=sys.stderr)
            continue

        publish_date = fm.get('publish_date')
        if publish_date is None:
            print(f"[publish_scheduled] No publish_date in {md_file}, skipping")
            continue

        # date 型ならそのまま、str なら parse
        if isinstance(publish_date, str):
            try:
                publish_date = date.fromisoformat(publish_date)
            except ValueError as e:
                print(f"[publish_scheduled] Invalid publish_date '{publish_date}' in {md_file}: {e}", file=sys.stderr)
                continue
        elif not isinstance(publish_date, date):
            print(f"[publish_scheduled] Invalid publish_date type in {md_file}: {type(publish_date)}", file=sys.stderr)
            continue

        if publish_date > today:
            print(f"[publish_scheduled] {md_file.name}: publish_date={publish_date} > today, skipping")
            continue

        # 公開対象
        slug = fm.get('slug') or md_file.stem
        new_filename = f"{publish_date.isoformat()}-{slug}.md"
        new_path = POSTS_DIR / new_filename

        # front matter 修正: date を publish_date に揃える、publish_date 削除
        fm['date'] = publish_date
        del fm['publish_date']

        new_content = serialize_front_matter(fm, body)

        # 書き込み + 旧ファイル削除
        new_path.write_text(new_content, encoding='utf-8')
        md_file.unlink()

        print(f"[publish_scheduled] Published: {md_file.name} -> {new_filename}")

        article_url = f"{SITE_BASE_URL}/articles/{slug}/"
        published.append({
            'slug': slug,
            'title': fm.get('title', ''),
            'description': fm.get('description', ''),
            'category': fm.get('category', ''),
            'url': article_url,
            'line_message': fm.get('line_message', ''),
        })

    set_output('published_count', len(published))

    # GAS への通知（各記事ごとに1リクエスト）
    if published and GAS_WEBHOOK_URL:
        for article in published:
            notify_gas(article)
    elif published and not GAS_WEBHOOK_URL:
        print("[publish_scheduled] GAS_WEBHOOK_URL not set, skipping notifications", file=sys.stderr)

    print(f"[publish_scheduled] Done. Published {len(published)} article(s).")


def notify_gas(article):
    """GAS Web App に HTTP POST で公開通知。"""
    payload = {
        'event': 'ARTICLE_PUBLISHED',
        'secret': ARTICLE_PUBLISH_SECRET,
        'slug': article['slug'],
        'title': article['title'],
        'description': article['description'],
        'category': article['category'],
        'url': article['url'],
        'line_message': article['line_message'],
    }

    try:
        # GAS Web App は最終 URL までリダイレクトされる場合があるので follow_redirects 維持
        response = requests.post(
            GAS_WEBHOOK_URL,
            json=payload,
            timeout=60,
            allow_redirects=True,
        )
        if response.status_code == 200:
            print(f"[notify_gas] OK for {article['slug']}: {response.text[:200]}")
        else:
            print(
                f"[notify_gas] Failed for {article['slug']}: "
                f"{response.status_code} {response.text[:200]}",
                file=sys.stderr,
            )
    except Exception as e:
        print(f"[notify_gas] Exception for {article['slug']}: {e}", file=sys.stderr)


def set_output(name, value):
    """GitHub Actions の output 設定。"""
    output_file = os.environ.get('GITHUB_OUTPUT')
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"{name}={value}\n")


if __name__ == '__main__':
    main()
