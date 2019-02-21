
# クリーンアーキテクチャー

## ワークショップのゴール

- クリーンアーキテクチャーの概要がわかる
- 具体的な実装イメージが湧く

## 何が嬉しいのか

```
フレームワーク非依存：アーキテクチャは，機能満載のソフトウェアのライブラリに依存していない．これにより，システムをフレームワークの制約で縛るのではなく，フレームワークをツールとして使用できる．
テスト可能：ビジネスルールは，UI，データベース，ウェブサーバー，その他の外部要素がなくてもテストできる．
UI非依存：UIは，システムのほかの部分を変更することなく，簡単に変更できる．たとえば，ビジネスルールを変更することなく，ウェブUIはコンソールUIに置き換えることができる．
データベース非依存：OracleやSQL ServerをMongo，BigTable，CouchDBなどに置き換えることができる．ビジネスルールはデータベースに束縛されていない．
外部エージェント非依存：ビジネスルールは外界のインターフェースについて何も知らない．
```

## 参考資料

- [5分でわかるクリーンアーキテクチャ](https://www.slideshare.net/kenjitanaka58/5-66290992)
- [ドメイン駆動設計で実装を始めるのに一番とっつきやすいアーキテクチャは何か\[DDD\] \- little hands' lab](https://little-hands.hatenablog.com/entry/2017/10/04/231743)
- [実装クリーンアーキテクチャ \- Qiita](https://qiita.com/nrslib/items/a5f902c4defc83bd46b8)
- [持続可能な開発を目指す ~ ドメイン・ユースケース駆動（クリーンアーキテクチャ） \+ 単方向に制限した処理 \+ FRP \- Qiita](https://qiita.com/kondei/items/41c28674c1bfd4156186)

## sample ソース

- 勉強のため[リファクタリングして学ぶTypeScriptでクリーンアーキテクチャ \- Qiita](https://qiita.com/kotauchisunsun/items/ec6b4086abe670c478fe)よりコピペ

- nodejsの環境構築

- パッケージインストール

```
npm i readline
npm i process
```

- ビルドと実行

```
tsc sample.ts
node sample.js
```

