from app import db
from flask import jsonify
from app.models.user import User
from app.service.user_service import create_user_service


# ユーザー作成
def create_login_controller(data):
    if "username" not in data or "password" not in data:
        return jsonify({"error": "username and password are required"}), 400

    user = User.query.filter_by(username=data["username"]).first()
    if user is not None:
        return jsonify({"error": "username already exists"}), 400

    res = create_user_service(data)
    return res