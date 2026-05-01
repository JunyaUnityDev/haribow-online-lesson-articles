# 記事制作依頼:フリッキーとトップが探るHIPHOPの起源

## 背景

HARIBOW Online Lesson の文化(culture)カテゴリ初記事。
対話形式で書く事を許容している例外的な記事カテゴリ。

JUNYA が過去に note 用に書いた原文をベースに、HARIBOW Online Lesson 用に最適化する。
キャラクター設定は CLAUDE.md(子)の「## キャラクター設定」セクション参照。

## 基本情報

- **タイトル**:フリッキーとトップが探るHIPHOPの起源
- **カテゴリ**:culture(文化 / 歴史)
- **スラッグ**:hiphop-origin
- **想定公開日**:後日(JUNYA 判断)
- **ファイル配置先**:`_drafts/hiphop-origin.md`(_posts/ ではなく _drafts/ に配置)

## Front Matter

```yaml
---
layout: article
title: "フリッキーとトップが探るHIPHOPの起源"
description: "団地の一室から始まった革命と、あなたの跳び方を変えるハークの哲学"
date: 2026-05-01
category: culture
slug: hiphop-origin
order: 5
---
```

注意:`date` は今日の日付を仮で入れる。公開時に JUNYA が決めた日付に変更し、`_posts/2026-XX-XX-hiphop-origin.md` にリネーム移動する想定。

## 記事の核(再掲、忘れないこと)

```
読者(HARIBOW受講者)に伝えたい3つの価値:
1. ヒップホップの起源(1973年8月11日に何が起きたか)
2. ダブルダッチが背負っている文化的な重み
3. あなたの「跳び方」を変える、ハークの哲学
```

## キャラクター運用(必読)

CLAUDE.md(子)の「## キャラクター設定」を必ず参照。

### この記事のキャスティング

- **メイン:フリッキー(質問役) × トップ(語り役)**
- **ゲスト:なし**(マヤ・シャインは登場しない)

### セリフ調整方針

JUNYA が過去に書いた原文(下記「記事原文」セクション)をベースに、口癖だけ自然に差し込む。

**意味は変えない、口癖を1〜2語足すだけ**。

例:
- 原文:「えぇ!?団地の一部屋ぁ!?そんなとこから!?」
- 調整:「えぇ!?団地の一部屋ぁ!?マジで?そんなとこから!?」(「マジで?」を1個足しただけ)

#### フリッキーの口癖(差し込み候補)

- 「マジで?」
- 「やばっ」
- 「すげーすげー」
- 「いやそれ知らんかった…」
- 「えっ待って待って」

#### トップの口癖(差し込み候補)

- 「フッ…」(笑う前に必ず言う)
- 「いいか、若いの」
- 「お前、それ本気で言ってんのか?」(目は笑ってる)

### 一人称・二人称

- フリッキー:オレ / お前(対トップは「トップさん」)
- トップ:俺 / お前(フリッキーには「お前」)

### キャラの軸を意識する

- フリッキー:カッコつけてるけど、根は純粋(感動して泣くタイプ)
- トップ:強面で無口、でも本当はめちゃくちゃ優しい

## 出力形式

### 全体構造

```
1. タイトル(Front Matter で指定済み)
2. リード文(冒頭の引き、3つの手に入るもの)
3. プロローグ(対話開始)
4. 🧠 第一章:ジャマイカから来た"静かな革命児"
5. 🎒 第二章:妹の制服から始まった夜
6. 🎛 第三章:1520 Sedgwick Avenue の夜
7. 💭 第四章:ハークの想い
8. 🌍 エピローグ:団地の部屋から世界へ
9. 📚 参考・出典
```

### 対話形式の書き方

`_includes/character.html` を使用。

```liquid
{% include character.html name="flekky" position="left" text="セリフ" %}
{% include character.html name="top" position="right" text="セリフ" %}
```

- フリッキーは `name="flekky"`、`position="left"`
- トップは `name="top"`、`position="right"`
- セリフ内の改行は `<br>` で表現するか、自然な区切りで分割する

### 章タイトルの書き方

```markdown
## 🧠 第一章:ジャマイカから来た"静かな革命児"

## 🎒 第二章:妹の制服から始まった夜

## 🎛 第三章:1520 Sedgwick Avenue の夜

## 💭 第四章:ハークの想い

## 🌍 エピローグ:団地の部屋から世界へ
```

### 強調の書き方

- 重要な用語(DJ Kool Herc、Apache、Peace, Love, Unity, and Having Fun)は `**bold**`
- 引用や心に残るフレーズは `> 引用` 形式

### 画像

**今回は画像なしで完成させる**。後日 JUNYA が画像追加する予定。
プレースホルダーや「※画像予定」の記述は **入れない**(対話のテンポを優先)。

---

## 記事原文(JUNYA が過去に書いたもの、これをベースにする)

以下が原文。**意味とトーンを尊重し、口癖だけ自然に差し込む**。

````
🎬【タイトル】
「のぶ太とJay-AnのHIPHOP大冒険 —団地の一室から始まった革命—」

👦 のぶ太:「なぁJay-An〜、ダブルダッチの人たちってさ、"ヒップホップ"ってよく言うじゃん。
 あれって何?音楽のこと?ファッション?それともダンスの名前なの?」
💪 Jay-An:「フッ…のぶ太、そんなことも知らねぇでロープ回してたのかよ!
 いいか、今や世界中に響く"ヒップホップ(Hip Hop)"って言葉…
 始まりは、ニューヨークの"団地の一部屋"なんだ。」
👦 のぶ太:「えぇ!?団地の一部屋ぁ!?そんなとこから!?」
💪 Jay-An:「そうだ。1970年代のはじめ、ニューヨークのブロンクス。
 そこは貧困と暴力にまみれた街だった。
 工場は閉まり、仕事はなくなり、家も壊れ、ギャングが支配していた。
 ドラッグが蔓延し、路上には使い捨てられた命が転がってた。
 黒人やラテン系の若者たちは、理由もなく警察に殴られ、逮捕された。
 "お前が貧しいのは自業自得だ"って、誰も助けてくれなかった。」
👦 のぶ太:「……そんな世界で、生きるだけでも大変じゃん。」
💪 Jay-An:「あぁ。
 政府もマスコミも、あの街を"見捨てた"。
 焼け落ちたビルが立ち並ぶ様子は"ブロンクス・バーニング"って呼ばれてな、
 夜になると炎が街を照らしてた。
 でも、そんな地獄の中で、"音"だけが希望だったんだ。」

🧠 第一章:ジャマイカから来た"静かな革命児"
💪 Jay-An:「そんな街に、一人の青年がいた。名前はクール・ハーク(DJ Kool Herc)。
 彼はジャマイカ生まれで、子どもの頃から"サウンドシステム"の文化の中で育った。
 街にスピーカーを並べて爆音を鳴らし、MCが群衆を盛り上げる。
 音で人の心を動かす——それが彼の原点だった。」
👦 のぶ太:「明るい国から来たんだね。」
💪 Jay-An:「そう。でもブロンクスに来てからは孤独だった。
 暴力と差別に囲まれて、誰も夢なんて語らない。
 それでもハークは思ってた。"音楽なら人を笑顔にできる"ってな。
 無口でおとなしいけど、芯が強い。
 彼の中には、音で世界を変えたいって火がくすぶってた。」

🎒 第二章:妹の制服から始まった夜
💪 Jay-An:「1973年8月11日。
 ハークは妹・シンディが"新学期の制服を買うため"に、少しでもお金を稼ごうと、
 団地の共有ルームでパーティーを開いた。
 名前は"Back to School Jam(バック・トゥ・スクール・ジャム)"。
 入場料は女の子25セント、男の子50セント。
 ほんの小さなチャリティーイベントさ。
 でも、その夜——世界が変わった。」
👦 のぶ太:「たったそれだけの理由から…?」
💪 Jay-An:「あぁ。
 生活のためのささやかなパーティーが、ヒップホップの始まりになったんだ。」

🎛 第三章:1520 Sedgwick Avenueの夜
💪 Jay-An:「場所は1520セジウィック・アベニュー。
 コンクリートの床、チカチカ光る蛍光灯、汗とタバコの匂い。
 でもハークはその狭い部屋に、手作りのスピーカーを並べて2台のターンテーブルを置いた。
 そして、レコードの中の"ドラムだけの部分(ブレイク)"を、交互に繋いで永遠に流した。
 それまで誰もやったことがなかった。
 会場の空気が変わった。
 子どもたちは体をひねり、回転し、床に手をついて踊り始めた。
 "暴力"のかわりに、"踊り"で叫んだんだ。
 『オレたちはここにいる!』って。」
👦 のぶ太:「団地の部屋が…希望のステージになったんだね。」
💪 Jay-An:「そうだ。
 そして、ハークが流していたのが "The Incredible Bongo Band" の "Apache(アパッチ)" だ。
 この曲のドラムブレイクが鳴り響いた瞬間、会場がひとつになった。
 のちに"ヒップホップの国歌"と呼ばれるこのビートに、
 みんなの心臓がシンクロした。
 それが、世界で最初の"ブレイクダンス"だったんだ。」
👦 のぶ太:「その曲が鳴って、みんなが一斉に踊り出す光景……
 想像するだけで鳥肌立つ!」
💪 Jay-An:「あの夜の"Apache"は、暴力も貧困も超えて、
 "オレたちは生きてる"って叫びに変わった。
 その一曲が、ヒップホップを生んだんだ。」

💭 第四章:ハークの想い
👦 のぶ太:「でもさ、ハークはなんでそんなに音にこだわったんだろう。」
💪 Jay-An:「彼はこう言ってた。
 "俺たちはテレビにも新聞にも出られない。でも音なら誰にも止められない。"
ハークは信じてた。
 『音の中では誰もが平等だ。』
 ギャングも、貧乏も、移民も関係ない。踊れば、ひとつになれる。
 それが、ヒップホップという名の"希望の言語"だった。」
👦 のぶ太:「……Jay-An、なんか胸が熱い。」
💪 Jay-An:「それでいい。
 ヒップホップは涙と汗と希望の上に立ってる。
 "Peace, Love, Unity, and Having Fun(ピース・ラブ・ユニティ・アンド・ハビング・ファン)"——
 平和、愛、団結、そして楽しむこと。
 それがハークの魂だ。」

🌍 エピローグ:団地の部屋から世界へ
💪 Jay-An:「その一夜が、アフリカ・バンバータ、グランドマスター・フラッシュ、
 そして世界中のダンサー、DJ、ラッパーたちへと火を広げた。
 お前が今ロープを回してるそのリズムの中にも、"Apache"のビートが生きてるんだぜ。」
👦 のぶ太:「……すげぇ。
 団地の部屋で鳴ったあのビートが、今オレの足のリズムになってるなんて!」
💪 Jay-An:「そうだ、のぶ太。
 お前も"次のブレイク"を作れ。
 ロープを回せ、魂を燃やせ、そして叫べ——
 "We are here!(ウィー・アー・ヒア!)"」
👦 のぶ太:「うぉぉぉぉ!!オレもハークみたいに、自分のヒップホップを生み出すぞーー!!」
````

---

## 出力すべき記事の完全版

下記がそのまま `_drafts/hiphop-origin.md` に配置すべき内容。
原文をベースに、口癖を自然に差し込み、Jekyll の include 形式に整形。

````markdown
---
layout: article
title: "フリッキーとトップが探るHIPHOPの起源"
description: "団地の一室から始まった革命と、あなたの跳び方を変えるハークの哲学"
date: 2026-05-01
category: culture
slug: hiphop-origin
order: 5
---

この記事を読むと、3つのものが手に入る:

1. **ヒップホップの起源**(1973年8月11日に何が起きたか)
2. **ダブルダッチが背負っている文化的な重み**
3. **あなたの「跳び方」を変える、ハークの哲学**

---

## プロローグ

{% include character.html name="flekky" position="left" text="なぁトップさん〜、ダブルダッチの人たちってさ、『ヒップホップ』ってよく言うじゃん。あれって何?音楽のこと?ファッション?それともダンスの名前なの?" %}

{% include character.html name="top" position="right" text="フッ…お前、そんなことも知らねぇでロープ回してたのかよ。いいか、若いの。今や世界中に響く『ヒップホップ(Hip Hop)』って言葉…始まりは、ニューヨークの『団地の一部屋』なんだ。" %}

{% include character.html name="flekky" position="left" text="えぇ!?団地の一部屋ぁ!?マジで?そんなとこから!?" %}

{% include character.html name="top" position="right" text="そうだ。1970年代のはじめ、ニューヨークのブロンクス。そこは貧困と暴力にまみれた街だった。工場は閉まり、仕事はなくなり、家も壊れ、ギャングが支配していた。ドラッグが蔓延し、路上には使い捨てられた命が転がってた。黒人やラテン系の若者たちは、理由もなく警察に殴られ、逮捕された。『お前が貧しいのは自業自得だ』って、誰も助けてくれなかった。" %}

{% include character.html name="flekky" position="left" text="……そんな世界で、生きるだけでも大変じゃん。" %}

{% include character.html name="top" position="right" text="あぁ。政府もマスコミも、あの街を『見捨てた』。焼け落ちたビルが立ち並ぶ様子は『ブロンクス・バーニング』って呼ばれてな、夜になると炎が街を照らしてた。でも、そんな地獄の中で、『音』だけが希望だったんだ。" %}

---

## 🧠 第一章:ジャマイカから来た"静かな革命児"

{% include character.html name="top" position="right" text="そんな街に、一人の青年がいた。名前は**クール・ハーク(DJ Kool Herc)**。彼はジャマイカ生まれで、子どもの頃から『サウンドシステム』の文化の中で育った。街にスピーカーを並べて爆音を鳴らし、MCが群衆を盛り上げる。音で人の心を動かす——それが彼の原点だった。" %}

{% include character.html name="flekky" position="left" text="明るい国から来たんだね。" %}

{% include character.html name="top" position="right" text="そう。でもブロンクスに来てからは孤独だった。暴力と差別に囲まれて、誰も夢なんて語らない。それでもハークは思ってた。『音楽なら人を笑顔にできる』ってな。無口でおとなしいけど、芯が強い。彼の中には、音で世界を変えたいって火がくすぶってた。" %}

---

## 🎒 第二章:妹の制服から始まった夜

{% include character.html name="top" position="right" text="**1973年8月11日**。ハークは妹・シンディが『新学期の制服を買うため』に、少しでもお金を稼ごうと、団地の共有ルームでパーティーを開いた。名前は『Back to School Jam(バック・トゥ・スクール・ジャム)』。入場料は女の子25セント、男の子50セント。ほんの小さなチャリティーイベントさ。でも、その夜——世界が変わった。" %}

{% include character.html name="flekky" position="left" text="たったそれだけの理由から…?やばっ。" %}

{% include character.html name="top" position="right" text="あぁ。生活のためのささやかなパーティーが、ヒップホップの始まりになったんだ。" %}

---

## 🎛 第三章:1520 Sedgwick Avenue の夜

{% include character.html name="top" position="right" text="場所は**1520セジウィック・アベニュー**。コンクリートの床、チカチカ光る蛍光灯、汗とタバコの匂い。でもハークはその狭い部屋に、手作りのスピーカーを並べて2台のターンテーブルを置いた。そして、レコードの中の『ドラムだけの部分(ブレイク)』を、交互に繋いで永遠に流した。それまで誰もやったことがなかった。会場の空気が変わった。子どもたちは体をひねり、回転し、床に手をついて踊り始めた。『暴力』のかわりに、『踊り』で叫んだんだ。『オレたちはここにいる!』って。" %}

{% include character.html name="flekky" position="left" text="団地の部屋が…希望のステージになったんだね。" %}

{% include character.html name="top" position="right" text="そうだ。そして、ハークが流していたのが **The Incredible Bongo Band** の **「Apache(アパッチ)」** だ。この曲のドラムブレイクが鳴り響いた瞬間、会場がひとつになった。のちに『ヒップホップの国歌』と呼ばれるこのビートに、みんなの心臓がシンクロした。それが、世界で最初の『ブレイクダンス』だったんだ。" %}

{% include character.html name="flekky" position="left" text="その曲が鳴って、みんなが一斉に踊り出す光景……すげー、想像するだけで鳥肌立つ!" %}

{% include character.html name="top" position="right" text="あの夜の『Apache』は、暴力も貧困も超えて、『オレたちは生きてる』って叫びに変わった。その一曲が、ヒップホップを生んだんだ。" %}

---

## 💭 第四章:ハークの想い

{% include character.html name="flekky" position="left" text="でもさ、ハークはなんでそんなに音にこだわったんだろう。" %}

{% include character.html name="top" position="right" text="彼はこう言ってた。" %}

> "俺たちはテレビにも新聞にも出られない。でも音なら誰にも止められない。"

{% include character.html name="top" position="right" text="ハークは信じてた。『音の中では誰もが平等だ。』ギャングも、貧乏も、移民も関係ない。踊れば、ひとつになれる。それが、ヒップホップという名の『希望の言語』だった。" %}

{% include character.html name="flekky" position="left" text="……トップさん、なんか胸が熱い。" %}

{% include character.html name="top" position="right" text="それでいい。ヒップホップは涙と汗と希望の上に立ってる。**「Peace, Love, Unity, and Having Fun(ピース・ラブ・ユニティ・アンド・ハビング・ファン)」**——平和、愛、団結、そして楽しむこと。それがハークの魂だ。" %}

---

## 🌍 エピローグ:団地の部屋から世界へ

{% include character.html name="top" position="right" text="その一夜が、アフリカ・バンバータ、グランドマスター・フラッシュ、そして世界中のダンサー、DJ、ラッパーたちへと火を広げた。お前が今ロープを回してるそのリズムの中にも、『Apache』のビートが生きてるんだぜ。" %}

{% include character.html name="flekky" position="left" text="……すげぇ。団地の部屋で鳴ったあのビートが、今オレの足のリズムになってるなんて!" %}

{% include character.html name="top" position="right" text="そうだ、フリッキー。お前も『次のブレイク』を作れ。ロープを回せ、魂を燃やせ、そして叫べ——『We are here!(ウィー・アー・ヒア!)』" %}

{% include character.html name="flekky" position="left" text="うぉぉぉぉ!!オレもハークみたいに、自分のヒップホップを生み出すぞーー!!" %}

---

## 📚 参考・出典

### 起源・歴史

- [PBS: Birthplace of Hip-Hop — 1520 Sedgwick Ave](https://www.pbs.org/wgbh/americanexperience/features/hip-hop-1520-sedgwick-avenue/)
- [TeachRock: DJ Kool Herc Biography](https://teachrock.org/biography/dj-kool-herc/)
- [Encyclopaedia Britannica: Kool Herc](https://www.britannica.com/biography/DJ-Kool-Herc)
- [Vanity Fair: Hip Hop's Founding Father Speaks (2005)](https://www.vanityfair.com/news/2005/11/dj-kool-herc-hip-hop)

### 音楽

- The Incredible Bongo Band – Apache (1973):"ヒップホップの国歌" と呼ばれるブレイクビーツ
````

---

## 実装手順

1. `_drafts/hiphop-origin.md` を上記内容で作成
2. `git status` で確認
3. ローカルで `bundle exec jekyll serve --drafts` を起動して、`http://localhost:4000/haribow-online-lesson-articles/articles/hiphop-origin/` にアクセスして表示確認
   - キャラ画像が表示される
   - 吹き出しレイアウトが綺麗に出る
   - スマホ表示でも崩れない
4. ローカル確認 OK なら git add → commit → push
   - commit メッセージ:`Add HIPHOP origin article (draft, culture category)`
5. push 後、GitHub Actions ビルドが成功することを確認
   - 注意:`_drafts/` 配下の md は、デフォルトでは `--drafts` フラグなしのビルドでは公開されない
   - 公開時は `_posts/YYYY-MM-DD-hiphop-origin.md` にリネーム移動 + push が必要(これは将来 JUNYA が判断)

## 報告フォーマット

```markdown
## ヒップホップ起源 記事制作 完了報告

### 1. 作成したファイル
- _drafts/hiphop-origin.md(N文字)

### 2. ローカル動作確認
- jekyll serve --drafts での表示確認:[OK / 問題あり]
- キャラ画像表示:[OK / 問題あり]
- 吹き出しレイアウト:[OK / 問題あり]
- スマホ表示:[OK / 問題あり]

### 3. push & deploy
- commit:[ハッシュ]
- GitHub Actions ビルド:[成功/失敗]

### 4. JUNYA への確認依頼

下記URLは _drafts/ 配下のため、現状では本番サイトには表示されません。
ローカルプレビュー or 公開時に _posts/ に移動すれば本番に表示されます。

ローカルプレビュー手順:
cd /Users/apple/projects/haribow/haribow-online-lesson-articles
bundle exec jekyll serve --drafts
ブラウザで http://localhost:4000/haribow-online-lesson-articles/articles/hiphop-origin/ にアクセス

公開する時は:
1. _drafts/hiphop-origin.md → _posts/YYYY-MM-DD-hiphop-origin.md にリネーム移動
2. git add → commit → push
3. GitHub Actions ビルド完了後、本番URLで公開
4. USER_BOOK の「記事ストック」シートで該当行のステータスを「公開済み」に更新
   公開URL列に https://junyaunitydev.github.io/haribow-online-lesson-articles/articles/hiphop-origin/ を記入

### 5. 既知の限界
- 画像なし(後日 JUNYA が追加予定:Kool Herc 写真、ブロンクス団地、Apache ジャケット 等)
- スプシの「記事ストック」シートにこの記事をネタ登録するのは別タスク
- 公開時の日付は仮(2026-05-01)、JUNYA が公開タイミングを決める時に修正
```

---

## 重要な制約

### やってはいけないこと

- **記事原文の意味やトーンを大きく変えない**(JUNYA が過去に書いたもの)
- 既存4記事(_posts/ 配下)に影響を与えない
- 既存の CSS、レイアウトを変更しない
- `_posts/` には配置しない(下書きとして `_drafts/` のみ)

### 必ずやること

- 口癖の差し込みは原文の意味を変えない範囲で(1〜2語追加程度)
- Jekyll の `{% include character.html %}` 形式で対話を記述
- フロント・マターは指定通り
- 重要な用語(DJ Kool Herc、Apache、Peace, Love, Unity, and Having Fun)は `**bold**`
- ローカル `jekyll serve --drafts` で動作確認

### 期待するセリフ調整の範囲

原文をかなり忠実に守る。

✅ OK 例:
- 「えぇ!?団地の一部屋ぁ!?そんなとこから!?」
   → 「えぇ!?団地の一部屋ぁ!?マジで?そんなとこから!?」(「マジで?」を1個追加)

❌ NG 例:
- 「えぇ!?団地の一部屋ぁ!?そんなとこから!?」
   → 「マジで!?団地の一部屋!?やばっ、すげーすげー、そんなとこから!?マジで!?」(口癖入れすぎて原文が壊れる)

口癖は1セリフあたり多くて1〜2個まで。

## 期待する成果

- _drafts/hiphop-origin.md が完成
- ローカルでプレビュー確認、対話形式と画像表示が正しく動作
- 後日 JUNYA が _posts/ にリネーム移動するだけで公開できる状態
- 文化(culture)カテゴリの初記事として、HARIBOW Online Lesson の世界観を1段階深める
