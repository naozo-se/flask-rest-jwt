from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.controller.user_controller import create_login_controller
from app.controller.auth_controller import login_controller
from app.utils.custom_log import get_logger, log

# ログオブジェクト生成
logger = get_logger()
# Blueprintオブジェクト生成
bp = Blueprint("api", __name__)
 
# リクエスト前処理
@bp.before_request
def log_request_info():
    logger.info(f"Request started: {request.method} {request.path}")
    logger.info(f"Request data: {request.data}")


# リクエスト後処理
@bp.after_request
def log_response_info(response):
    logger.info(f"Exit Method:  {request.method} {request.path}")
    logger.info(f"Return Response:  {response}")
    return response


# ユーザー登録処理
@bp.route("/user", methods=["POST"])
def register():
    data = request.get_json() or {}
    res = create_login_controller(data)
    return res


# ログイン処理
@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    res = login_controller(data)
    return res


# jwt_requiredを指定すると、トークンのある認証しか処理ができない
@bp.route("/protected")
@jwt_required()
def protected():
    return jsonify({"message": "This is a protected route."}), 200
