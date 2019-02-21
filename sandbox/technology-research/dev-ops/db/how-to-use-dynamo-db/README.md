# how-to-use-dynamo-db

---

## 調査概要

### テーマ

- dynamo-dbを触ってみる

### 理由や背景

- なんか色々とDynamoDBが波に乗ってきた雰囲気?だったから触ってみようかな、と。
    - [\[速報\]待望のDynamoDBのトランザクションがリリースされました！](https://dev.classmethod.jp/cloud/aws/new-release-dynamodb-transactions/)
    - ローカルでも試せそう
      - [DynamoDB Localの公式Docker Imageが公開されました。](http://blog.serverworks.co.jp/tech/2018/08/29/dynamodb-local-dokcer/)
- あと、仕事で使うことになるかもしれない。わくわく

### ゴール

- ローカルにdynamodbの環境構築してみる
- 基本的なコマンドをいじってみる
- スクリプトから基本操作をさせる
    - テーブル作成スクリプト
    - データ流し込みスクリプト
    - データ取得時間計測スクリプト

---

# Dependency

## 動作確認済のバージョン

- nodeバージョン
    - v10.15.0

- npmバージョン
    - 6.7.0

---

# Setup

- dynamodbとMySQLコンテナ起動と確認

```
cd ./container
docker-compose up -d
docker ps -a
```

- dynamodbへのデータ作成

```
cd ./scripts


```

- Node

```
cd ./
npm i
npm run build
npm run start
```
---

# Usage

```
# 実行例
npm run start
```

---

# References(調査メモ)

## DynamoDBの概要

- [DynamoDB の基礎知識とまとめ \- Qiita](https://qiita.com/hshimo/items/e5ad98b21786d796f1da)
- [【AWS】今更ながらDynamoDB入門 \- Qiita](https://qiita.com/maaaato/items/4a0f5c1dcc78677973c9)

### 補足

- [KVS（Key\-Value Store）とは \- Qiita](https://qiita.com/uenohara/items/23eb6ee1259f8a927445)
- [NoSQLについて勉強する。 \- Qiita](https://qiita.com/t_nakayama0714/items/0ff7644666f0122cfba1)

---

## ローカルで動かす

- [aws\-sam\-localだって\!?これは試さざるを得ない\! \- Qiita](https://qiita.com/DeployCat/items/0e631029ae4ef41c0f3f)

- [AKIBA\.AWS 第10回 特別編で「DynamoDB Localを手軽に使える公式のDockerイメージ」を発表しました \#akibaaws ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/dynamodb-local-docker-image/)

### 補足

- [DynamoDB 使用に関する注意事項 \- Amazon DynamoDB](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.UsageNotes.html)

---

## aws cli

- [aws cli で DynamoDB を使う \- Qiita](https://qiita.com/ekzemplaro/items/93c0aef433a2b633ab4a)
- [CLI の使用 \- Amazon DynamoDB](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Tools.CLI.html)
- [AWS CLIで使える認証情報とオプションの設定方法まとめ ｜ DevelopersIO](https://dev.classmethod.jp/cloud/aws/how-to-configure-aws-cli/)

### ちょいハマりどころメモ

- 必要なくてもConfigの設定が必要っぽい

```
cat ~/.aws/config
[default]
region=us-west-2
output=json
```



