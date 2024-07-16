from flask import jsonify, session
from app.utils.auth import generate_token, authenticate_user


# ログイン処理
def login_service(data):
    user = authenticate_user(data["username"], data["password"])
    if user:
        # 認証OKの場合、指定ユーザーのトークン作成
        access_token = generate_token(user)
        # 指定ユーザーのトークンを返す
        return jsonify({"access_token": access_token}), 200
    else:
        # ユーザー情報が取得できていない場合はエラーレスポンスを返す
        return jsonify({"error": "invalid username or password"}), 401
