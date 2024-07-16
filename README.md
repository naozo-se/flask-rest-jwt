# Flask Rest 環境

## 環境
- Docker 26.0.0
- Docker Compose v2.26.1
- python 3.12.4 (デフォルトは3.12の最新を取得)
- Flask 3.0.3

## その他環境(ピックアップ)
- SQLAlchemy(To PostgreSQL)
- JWT(Flask-JWT-Extended)

## 起動方法
```shell
docker compose up -d --build
```

## 動作確認
```shell
# ユーザー作成
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' http://127.0.0.1:5000/api/user

# ログイン処理
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' http://127.0.0.1:5000/api/login

# ログイン後確認(APIKEYは、帰ってきたキーを指定)
curl -H "Authorization: Bearer APIKEY" http://127.0.0.1:5000/api/protected
```

## 注意点（今後の対応予定）
- ユーザー登録は、初回登録する
- ログアウトがない(JWTの仕組みが意外と困難)
