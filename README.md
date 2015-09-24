### タスク継続支援

![Images](http://cdn-ak.f.st-hatena.com/images/fotolife/r/rinne_grid2_1/20150914/20150914070629.png)

* Webアプリケーション
* 事前に登録されたタスクを選択し、クリックだけで記録する
* 簡易なメモ書きを同時に登録する
* 終了したタスクはチェックをつけ、完了させる


This is Web Application for the "tasks" continuation,
not task management application.

You can select the general "tasks",
and these progress checks for yourself.

### 必要なもの

* Python3.x
* Django1.8.4
* CoffeeScript
* Node.js

### 実行について
```shell
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ (venv) pip install Django==1.8.4
$ (venv) cd taskskill
$ (venv) python manage.py runserver
```

### アプリケーションログイン

* アプリURL
  * http://localhost:8000/tasks/index
* ログイン
  * ユーザー：main
  * パスワード：main

### adminログイン

* adminURL
  * http://localhost:8000/admin
* ログイン
  * ユーザー：main
  * パスワード：main
