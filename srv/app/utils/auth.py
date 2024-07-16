from flask_jwt_extended import create_access_token
from datetime import timedelta
from app.models.user import User


# ユーザー認証処理
def authenticate_user(username, password):
    # ユーザー情報取得
    user = User.query.filter_by(username=username).first()
    # パスワードチェック
    if user and user.check_password(password):
        return user
    # パスワードチェックNGの場合
    return None


# トークン生成
def generate_token(user):
    access_token = create_access_token(
        identity=user.id, 
        expires_delta=timedelta(hours=1)  # トークンの有効期限
    )
    return access_token