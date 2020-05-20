"""
app
"""

from pytest import fixture

from app.app import create_app, config


@fixture
def app():
    """test app"""
    # 配置 config
    config.TESTING = True
    config.SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI_TEST

    app = create_app()
    return app
