"""
db fixtures
"""

import redis
from pytest import fixture

from app.app import db
from app.utils.redis import pool

from . import app


@fixture
def clear_mysql(app: fixture):
    """清理 mysql 数据"""
    yield
    with app.app_context():
        db.session.commit()
        db.drop_all()


@fixture
def clear_redis():
    """清理 redis 数据"""
    yield
    r = redis.Redis(connection_pool=pool)
    r.flushdb()


@fixture
def clear_db(clear_redis: fixture, clear_mysql: fixture):
    """清理所有数据"""
    pass


@fixture
def init_db(app: fixture):
    """初始化数据库"""
    with app.app_context():
        db.create_all()
