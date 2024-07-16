from flask import jsonify
from app.service.auth_service import login_service


def login_controller(data):
    if "username" not in data or "password" not in data:
        return jsonify({"error": "username and password are required"}), 400

    res = login_service(data)
    return res
