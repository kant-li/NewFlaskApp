"""
应用入口，提供工厂函数
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_mail import Mail

from config import config

db = SQLAlchemy()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    mail.init_app(app)
    Swagger(app)

    from .apis.user import user

    app.register_blueprint(user)

    return app
