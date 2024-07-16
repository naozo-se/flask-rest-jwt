from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import timedelta
from dotenv import load_dotenv
import os


# .env ファイルをロード
load_dotenv("app.env")

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    # .envファイルから環境変数をロード
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DB')}'

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
