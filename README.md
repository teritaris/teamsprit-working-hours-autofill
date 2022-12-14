# teamsprit-working-hours-autofill
## Overview
TeamSpiritで#1タスクの工数を全日100%で入力するやつ

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
