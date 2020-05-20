"""
tests for user api
"""
import json
from pytest import mark, fixture

from app.utils.redis import redis_get_str

from tests.fixtures import *
from tests.constants import (
    TEST_EMAIL,
    TEST_PASSWORD,
    TEST_USERNAME,
    SEND_VERIFICATION_CODE_URL,
    REGISTER_URL,
    LOGIN_URL,
    TOKEN_TEST_URL,
)


@mark.user
def test_send_verification_code(
    client: fixture, mock_verification_code_email: fixture, clear_db: fixture
) -> None:
    url = SEND_VERIFICATION_CODE_URL

    # 没有数据
    r = client.get(url)
    assert r.status_code == 400
    response_data = json.loads(r.get_data())
    assert "Invalid email address" in response_data.get("message")

    # 错误的邮箱
    query = {"email": "@test.com"}
    r = client.get(url, query_string=query)
    assert r.status_code == 400
    response_data = json.loads(r.get_data())
    assert "Invalid email address" in response_data.get("message")

    # 正确的邮箱
    query = {"email": TEST_EMAIL}
    r = client.get(url, query_string=query)
    assert r.status_code == 200
    response_data = json.loads(r.get_data())
    assert "verification code" in response_data.get("message")


@mark.user
def test_register(
    client: fixture,
    mock_verification_code_email: fixture,
    clear_db: fixture,
    init_db: fixture,
) -> None:
    # 获取验证码
    r = client.get(SEND_VERIFICATION_CODE_URL, query_string={"email": TEST_EMAIL})
    assert r.status_code == 200
    code = redis_get_str(TEST_EMAIL)

    # 尝试注册
    post_data = {
        "verification_code": code,
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD,
        "username": TEST_USERNAME,
    }
    r = client.post(REGISTER_URL, data=post_data)
    assert r.status_code == 200
    response_data = json.loads(r.get_data())
    assert len(response_data.get("data", {}).get("token")) > 0


@mark.user
def test_login(
    client: fixture,
    mock_verification_code_email: fixture,
    clear_db: fixture,
    insert_test_user: fixture,
):
    # 尝试登录
    post_data = {"email": TEST_EMAIL, "password": TEST_PASSWORD}
    r = client.post(LOGIN_URL, data=post_data)
    assert r.status_code == 200
    response_data = json.loads(r.get_data())
    assert len(response_data.get("data", {}).get("token")) > 0

    # 密码错误
    post_data = {"email": TEST_EMAIL, "password": ""}
    r = client.post(LOGIN_URL, data=post_data)
    assert r.status_code == 400
    response_data = json.loads(r.get_data())
    assert "Invalid email or password" in response_data.get("message", "")

    # 用户不存在
    post_data = {"email": "wrong_user", "password": TEST_PASSWORD}
    r = client.post(LOGIN_URL, data=post_data)
    assert r.status_code == 400
    response_data = json.loads(r.get_data())
    assert "User not exists" in response_data.get("message", "")

    # 空用户名
    post_data = {"email": "", "password": TEST_PASSWORD}
    r = client.post(LOGIN_URL, data=post_data)
    assert r.status_code == 400
    response_data = json.loads(r.get_data())
    assert "User not exists" in response_data.get("message", "")


@mark.user
def test_token_test(client: fixture, login_client: fixture):
    # 未登录用户无法访问
    r = client.get(TOKEN_TEST_URL)
    assert r.status_code == 401
    response_data = json.loads(r.get_data())
    assert "Unauthorized" in response_data.get("message", "")

    # 带token可以访问
    r = login_client.get(TOKEN_TEST_URL, headers=login_client.headers)
    assert r.status_code == 200
    response_data = json.loads(r.get_data())
    assert "token verified" in response_data.get("message", "")
