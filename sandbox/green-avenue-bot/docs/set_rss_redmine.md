## Slack + Redmine 連携
### 設定手順
1. 通知対象Redmineの "活動" or "チケット" ページにアクセス
2. ページ最下部の右側にある `他の形式にエクスポート: Atom` をクリック

![atom](https://user-images.githubusercontent.com/38580845/62068686-81308500-b271-11e9-8565-6ed4345d945d.png)

3. 取得できるXMLが表示される。このページのURL(下の画像赤枠)をコピーしてメモっておく。<br>
※) URLパラメータ(?key=以降の部分)は省略する。<br>
※) https:// が認証されない場合は、一旦http:// に書き換えて。

![atom_xml](https://user-images.githubusercontent.com/38580845/62068801-c81e7a80-b271-11e9-8cc0-b7b85e116d51.png)

4. Slackデスクトップアプリに移動
5. `+アプリを追加する` をクリック

![slackapp](https://user-images.githubusercontent.com/38580845/62069208-b4bfdf00-b272-11e9-9e45-312d60f431aa.png)

6. アプリ一覧 から RSS を選択

![slackapp_rss](https://user-images.githubusercontent.com/38580845/62069337-02d4e280-b273-11e9-9591-a8f14458d603.png)

7. フィードURLに 3. でメモったURLをペースト
8. チャンネルへの投稿で通知したいルーム名を選択
9. このフィードを購読するを押下(無料だからね！！)

![slackapp_rss_add](https://user-images.githubusercontent.com/38580845/62069453-416a9d00-b273-11e9-9eb9-b305e60264b9.png)

10. これにてRedmine通知連携は完了。
