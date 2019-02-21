# kanborad

## 調査テーマ

- GithubのProjects(カンバン)をターミナルから操作する方法

## 背景

- トラックバッドをOFFっている花屋PCとGUIでのカンバン操作の相性の悪さ
    - GUI操作の撲滅運動

---

## 調査メモ

- [yuichi1004/kanc: Kanboard remote CUI client](https://github.com/yuichi1004/kanc)
    - SSHキー設定が必要になる
      - 仕事PCから業務アカウントと私物アカウントの使い分けをどうするか
        - ちょい調査と設定面倒くさそう


- [smallhadroncollider/taskell: Command\-line Kanban board/task manager with support for Trello boards and GitHub projects](https://github.com/smallhadroncollider/taskell)
    - ローカルなら動かせそう
    - Githubとの連携周りでいしゅー報告せよ的なエラー発生中
        - 惜しい...うーん、調べてOSSにPR出してみる？
        ```bash
        taskell -g repos/hanaya-san/gardening ./github.md
        ```

- [\[wip\] Git・Githubをより強力にするためのCLIツール \- Qiita](https://qiita.com/unbabel/items/6bb651d55c9b7620cb61)

- [Projects \| GitHub Developer Guide](https://developer.github.com/v3/projects/)
    - このAPIをラップするツール作った方がもはや早そう

---

## カンバン操作方法の構築案

- [Projects \| GitHub Developer Guide](https://developer.github.com/v3/projects/)
    - 以下、２点が可能なCLIツールをラップする
        - Github上のデータをtaskellが読み書き出来る形式でのインポート
        - taskellで編集したデータのアップロード

- [smallhadroncollider/taskell: Command\-line Kanban board/task manager with support for Trello boards and GitHub projects](https://github.com/smallhadroncollider/taskell)
    - インポートしたファイルをこれを使って編集する


- あ、でもいしゅーはどうしよう...

- 諦めるかねぇ、面倒くさい...

---

## 蛇足

- [GitHub Project に自動でカードのカラム遷移をする機能が追加された \- Qiita](https://qiita.com/matsubara0507/items/f384991b4854aa28745a)
    - 関係ないけど、設定すると便利そう

- [haskellcamargo/sclack: The best CLI client for Slack, because everything is terrible\!](https://github.com/haskellcamargo/sclack)
    - 面白そうなSlackCLI発見


