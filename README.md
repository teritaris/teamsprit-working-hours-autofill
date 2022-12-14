# teamsprit-working-hours-autofill
## Overview
TeamSpiritで#1タスクの工数を全日100%で入力するやつ
![inputwindow](https://user-images.githubusercontent.com/14288406/207502045-c5d6e2e1-99c7-42be-bda1-cd350a8fb949.png)

## Usage
username.pyにユーザ情報を入力
```
name    : ログインユーザ名
password: ログインユーザパスワード
```

Dockerコンテナを起動

`$ docker-compose up -d`

100%入力実行

`$ docker exec python3 python opt/main_headless.py`

未入力状態に戻す

`$ docker exec python3 python opt/reset.py`
