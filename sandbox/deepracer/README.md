# deepracer レース出場に向けての調査

---

## 概要

- 背景

```
2018/11/28(Wed) 米ラスベガスで開催されたAWSの開発者イベント"re:Invent 2018"の中で"AWS DeepRacer"が発表された。
"DeepRacer"とは機械学習(強化学習)モデルを組み込んで自律走行できる、1/18スケールのAI搭載レーシングカー。
クラウド上のシミュレータでトレーニングした学習モデルでバーチャルカーとレースさせたり、現実世界で走らせたりすることもできる。
"AWS DeepRacer League"なんていうレースの世界大会も予定されているらしい。
```

- 目的
    - クラウドアーキテクチャを学ぶ
        - AWSの各種サービス色々さわって慣れておこう。
        - クラウド開発(サーバレス)についてかなり勉強になりそう。
    - IoTを学ぶ
        - IoTxAIについて知見広げよう。
        - 自動車業界のIoTはかなり最先端走ってるから色々勉強になること多いと思う。
    - 強化学習を学ぶ
        - 機械学習モデルを構築するためのノウハウを勉強しよう。
        - 数年後、[AIに仕事奪われる可能性](https://robo-school.net/future-of-employment-wayaku/)があるなら、逆にAI使う側に回ろうぜ！！
            - 2024年までにプログラマは48%の確率で淘汰される(らしい)
    - レース大会への参加
        - せっかくやるなら入賞したいよね。

---

## レース大会の概要

- 出場権
    - TODO: 要調査(オンラインで予選突破だったような？予選出場はいつまでに？とか)

- 採点基準
    - TODO: 要調査(アルゴリズム重視？最適化重視？レース結果Only？ソースも見られる？)

- 日時と場所
    - 予選
        - 2019年X月XX日までにX位以上
        - オンライン
    - 本選
        - 2019年X月XX日
        - 幕張メッセ

- 費用
    - 実機: $399
    - AWS: 都度課金  

---

## 開発手法・環境
- アーキテクチャ  
### クラウドアーキテクチャ
![cloud-architecture](https://github.com/hanaya-san/seed/blob/images/sandbox/deepracer/img/deepracer-training-service-architecture.jpg)

### ソフトウェアアーキテクチャ
![software-architecture](https://github.com/hanaya-san/seed/blob/images/sandbox/deepracer/img/deepracer-software-architecture.jpg)

### クリーンアーキテクチャーを採用したい
    - 概要: [クリーンアーキテクチャ\(The Clean Architecture翻訳\) \| blog\.tai2\.net](https://blog.tai2.net/the_clean_architecture.html)
        - ワークショップでも勉強&共有予定
    - 理由:
        - イケてる＆実践的
            - (過去の偉人たちが失敗と成功を積み上げてきたものの集大成とも呼べそうなアーキテクチャー。今後も使える)
        - 学習コストがかかるが、その分設計力がかなり上がるはず
- 開発フロー
    - 基本Githubフローでいきたい
    - TODO: 以下は話し合って決めたい
        - 独自のブランチ運用ルールが必要にならないか(特にシミュレーション確認手法周りで)
        - CIを導入出来るフローがないか(特にPR周りで)
            - CI化する優先度をどうするか。CIを導入しないと圧倒的に作業効率が落ちるか
- ローカルの実行環境
    - シミュレータ環境をローカルに構築するのはちょっと無理そう
    - 可能ならば最低限テストコード実行はローカルで確認可能としたい

---

## CI関連

### 何をCI化するか

- TODO: 後日決める

### (CI関連の調査or勉強すべき項目を必要に応じて追加)

- (必要に応じて別チケットで管理)


---

## Python関連

### Linter

- 別チケットで調査中

### テストコード

- 別チケットで調査中

### クリーンアーキテクチャーをPythonへの応用可否

- クリーンアーキテクチャーのワークショップ実施後に調査
    - MEMO: Hanayaの所感的にはイケるはず


---

## 機械学習関連

### 機械学習の概要

- TODO: いい感じの記事のリンクいくつか貼っておく
    - ワークショップ化するのもあり
    - これこそオンラインの授業あったりしそう

### (機械学習関連の調査or勉強すべき項目を必要に応じて追加)

- Hogehoge


---

## AWS関連

### AWS利用上のセキュリティ対策

- TODO: いい感じの記事のリンクいくつか貼っておく

### 使用するAWSサービス

| サービス名 | 概要 | 詳細リンク |
|:---|:---|:---|
|AWS IAM |認証情報管理 |準備中 |
|Amazon S3 |ストレージ |準備中 |
|AWS Lambda |サーバーレスコンピューティング |準備中 |
|AWS CloudFormation |AWSリソースのテンプレート化 |準備中 |
|Amazon SageMaker |機械学習 |準備中 |
|Amazon RoboMaker |ロボットアプリケーション |準備中 |
|Amazon Kinesis |ストリーミングデータ用プラットフォーム |準備中 |
|Amazon CloudWatch |リソースモニタリング |準備中 |

### 料金体系

#### 基本情報
- 無料枠について

#### 各種サービス
- AWS IAM
- Amazon S3
- AWS Lambda
- AWS CloudFormation
- Amazon SageMaker
- Amazon RoboMaker
- Amazon Kinesis
- Amazon CloudWatch


---

## 参考サイト リンク集

- [AWS\(クラウド\)超入門 第1回 \- Qiita](https://qiita.com/modokkin/items/fc1280eda4356816a3f9)
    - AWSの入門方法について

- [\#3 メンバー紹介とAWSの始め方 \[アマゾン主催の自動走行レースで世界一を目指すブログ\]｜Masaya Aso｜note](https://note.mu/masayaaso/n/ne3e71e9f845e)
    - ライバルチーム(こちらが勝手にそう思っているだけ)

- [AWS DeepRacerの実機をマニュアルモードで操作する \#reinvent ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/deep-racer-manual-mode/)
    - 実機手に入れたら、役に立ちそうな記事

- [AWS DeepRacerの購入と環境構築まで : テクノロジーウェアハウス](http://www.susanooo.net/archives/14592424.html)
    - ROSのことは書いてあるけどなぁ
    - ローカルでシミュレーション環境は厳しいそうな気がするんご
        - カメラは？ホイールは？マップは？

- [\[参加レポート\] AIM206 AWS DeepRacer ワークショップに参加してきました \#reinvent ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/reinvent2018-aim206-deepracer-workshop/)
    - ワークショップ参加で実機がもらえるだと！？！？

- [Donkey](https://www.slideshare.net/HoriTasuku/donkey-car)
    - AmazonではないけどGoogle版で自作してる人もおるみたいｗ

- [Comparing the Amazon DeepRacer & Donkey Car approach to Artificial Intelligence](https://medium.com/datadriveninvestor/comparing-the-amazon-deepracer-donkey-car-approach-to-artificial-intelligence-d46f0e155974)
    - Amazon vs Google の比較記事

