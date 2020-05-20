"""
models op
"""

from pytest import fixture

from app.models.user import User
from tests.constants import TEST_EMAIL, TEST_PASSWORD, TEST_USERNAME


@fixture
def insert_test_user(app: fixture, init_db: fixture):
    """写入测试用户"""
    with app.app_context():
        user = User(username=TEST_USERNAME, password=TEST_PASSWORD, email=TEST_EMAIL)
        user.save()
