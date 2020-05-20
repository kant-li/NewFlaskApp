"""
fixture flask client
"""

import json
from pytest import fixture

from tests.constants import TEST_EMAIL, TEST_PASSWORD, LOGIN_URL
from .app import app
from .data import insert_test_user


@fixture
def client(app: fixture):
    """test client"""
    return app.test_client()


@fixture
def login_client(app: fixture, client: fixture, insert_test_user: fixture):
    """test login client"""
    with app.app_context():
        data = {
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
        }

        res = client.post(LOGIN_URL, data=data)
        access_token = json.loads(res.get_data()).get("data", {}).get('token')
        assert len(access_token) > 0
        headers = {"Authorization": 'Bearer ' + access_token}
        client.token = access_token
        client.headers = headers
        return client
