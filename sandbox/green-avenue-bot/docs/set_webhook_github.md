## Slack + GitHub 連携
### 設定手順
1. Slackデスクトップアプリを開く
2. `+アプリを追加する` を選択

![slackapp](https://user-images.githubusercontent.com/38580845/62070552-ad4e0500-b275-11e9-8111-2ef3ee3ef101.png)

3. アプリ一覧から GitHub を選択 (Enterprise Server じゃないよ！)

![slackapp_github](https://user-images.githubusercontent.com/38580845/62070517-9a3b3500-b275-11e9-8431-76a7f3ac5395.png)

4. GitHub App をインストール (画像はOpen だけど、初期は Install になってる。)

![slackapp_github_install](https://user-images.githubusercontent.com/38580845/62070673-ed14ec80-b275-11e9-8be0-e636bc0d0eca.png)

5. Slack App に GitHubが追加されているので選択

![slackapp_github_bot](https://user-images.githubusercontent.com/38580845/62070736-103f9c00-b276-11e9-857a-0c09d7e0b5cb.png)

6. `/github signin` とslack上(GitHubルーム)で入力すると、ブラウザが開くので、そのまま認証させる。

![slackapp_github_permission](https://user-images.githubusercontent.com/38580845/62070802-32391e80-b276-11e9-8212-09a08adae46d.png)

7. 通知したいルームで `invite @GitHub` と入力して、GitHubを参加させる。

![slackapp_github_invite](https://user-images.githubusercontent.com/38580845/62071055-abd10c80-b276-11e9-8ed6-2b1a1f66a706.png)

8. `/github subscribe ${user}/${repo} ${option}` と入力してWebhookを有効にする。

![slackapp_github_notify](https://user-images.githubusercontent.com/38580845/62071175-e9ce3080-b276-11e9-9ddc-56af47d9d524.png)

### /github subscribe , unsubscribe コマンドの通知オプション設定について

`/github subscribe ${user}/${repo} ${option}` : ${option}の有効化<br>
`/github unsubscribe ${user}/${repo} ${option}` : ${option}の無効化<br>

指定できる ${option}は以下の通り。通知したい項目に合わせて、リポジトリごとに設定可能。

#### デフォルトで有効な設定
| コマンド | 内容 |
----|---- 
| issues | issues のOpenまたはCloseの通知 |
| pulls | 新規またはマージされたPR、及びドラフトPRと「レビューの準備完了」 |
| statuses | PRのステータスを通知 |
| commits | master ブランチへのコミットを通知 |
| deployments | デプロイに関する最新のステータス |
| public | privateからpublicに切り替わったリポジトリを通知 |
| releases | 公開されたリリース情報を通知 |

#### デフォルトでは無効な設定
| コマンド | 内容 |
----|---- 
| reviews | PRのレビュー通知 |
| comments | issuesに関する新しいコメントとPRを通知 |
| branches | 作成または削除されたブランチを通知 |
| commits:all | 全てのブランチへのコミットを通知 |

#### とりあえず全部通知したいなら
`issues, pulls,statuses,public,commits:all,releases,comments,branches,reviews` <br>
と指定すればOK
