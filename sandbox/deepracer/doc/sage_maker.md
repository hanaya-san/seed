# Amazon SageMaker

## 概要
機械学習の構築、学習、デプロイを行うためのサービス


## 開始方法
- Amazon公式サイトに日本語のドキュメントを発見したのでこちらを参照
  - [Amazon SageMaker - 仕組み](https://docs.aws.amazon.com/ja_jp/sagemaker/latest/dg/how-it-works.html)
  - [Amazon SageMaker - 開発者ガイド](https://docs.aws.amazon.com/ja_jp/sagemaker/latest/dg/gs.html)

- GUI設定・操作の分かりやすい記事
  - [【初心者向け】Amazon SageMakerではじめる機械学習 ](https://dev.classmethod.jp/machine-learning/getting-started-with-amazon-sagemaker/)

### トピック一覧
<details>
<summary>仕組み</summary>
- 1. Amazon SageMaker による機械学習<br>
- 2. Amazon SageMaker によるモデルのトレーニング<br>
- 3. Amazon SageMaker ホスティングサービスでモデルをデプロイする<br>
- 4. Amazon SageMaker ノートブックインスタンスを使用したデータの確認と前処理<br>
- 5. 機械学習モデルの検証<br>
- 6. Amazon SageMaker プログラミングモデル<br>
</details>
<details>
<summary>開始方法</summary>
- 1. セットアップ<br>
　- 1.1. AWS アカウントおよび管理ユーザーを作成する<br>
　　- 1.1.1. AWS アカウントの作成<br>
　　- 1.1.2. IAM 管理ユーザーの作成とサインイン<br>
　- 1.2. S3バケットを作成する<br>
- 2. Amazon SageMaker ノートブックインスタンスの作成<br>
- 3. 組み込みのアルゴリズムでモデルをトレーニングし、デプロイする<br>
　- 3.1. Juypter ノートブックを作成し、変数を初期化する<br>
　- 3.2. トレーニングデータをダウンロード、調査、および変換する<br>
　- 3.3. モデルをトレーニングする<br>
　- 3.4. Amazon SageMaker ホスティングサービスにモデルをデプロイする<br>
　- 3.5. モデルを検証する<br>
- 4. クリーンアップする<br>
- 5. 追加の考慮事項: インターネット接続アプリケーションへの Amazon SageMaker エンドポイントの結合
</details>


## 料金
### 無料利用枠
- 登録から２ヶ月間

#### notebook
- モデル構築用
  - t2.medium : 250時間/月 まで
- モデル学習用
  - m4.xlarge : 50時間/月 まで
- デプロイ用
  - m4.xlarge : 125時間/月 まで

しかし現時点で、上記の構成で使ってるだけなのに請求が若干来てるなぁ・・・($3だけど)  
まだまだ要調査

### 通常利用
#### 無料利用枠のまま使った場合を記載
- 利用リージョン
  - 米国西部(オレゴン)
- モデル構築用
  - ml.t2.medium : 5.104 [JPY/h]
- モデル学習用
  - ml.m4.xlarge : 30.8 [JPY/h]
- デプロイ用
  - ml.m4.xlarge : 30.8 [JPY/h]

#### 仮に、24時間フル稼働/月 で計算すると
- ml.t2.medium : 3,674  JPY (122.496/day x 30)
- ml.m4.xlarge : 22,176 JPY (739.2/day x 30)
- ml.m4.xlarge : 22,176 JPY (739.2/day x 30)

合計: `48,026 JPY`

コード検証とか細かいのはGoogleColaboratoryとか併用しないと死にそう  
まあ、無料枠をうまく使えば問題ないと思われる  
  
でも使い終わったらかならずインスタンスは落とそう！！！  

