from app.models.user import User
from app import db
from flask import jsonify


# ユーザー登録処理
def create_user_service(data):
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "user created successfully"}), 201
