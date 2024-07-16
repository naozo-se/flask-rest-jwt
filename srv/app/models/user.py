from app import db
from werkzeug.security import generate_password_hash, check_password_hash


# ユーザーテーブル（認証で利用）
class User(db.Model):
    # ID（主キー）
    id = db.Column(db.Integer, primary_key=True)
    # ユーザー名
    username = db.Column(db.String(64), index=True, unique=True)
    # パスワード(ハッシュで格納)
    password_hash = db.Column(db.String(256))

    # パスワードハッシュ化
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワード（ハッシュでチェックする）
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)
