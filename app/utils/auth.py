"""
auth functions
"""

from flask import g, request
from flask_httpauth import HTTPTokenAuth
from app.utils.utils import error_response
from app.models.user import User

auth = HTTPTokenAuth()


@auth. error_handler
def unauthorized():
    return error_response(status=401, message="Unauthorized.")


@auth.verify_token
def verify_token(token):
    """验证token"""
    g.user = None
    result = User.verify_auth_token(token)
    if not result:
        return False

    # 将用户信息写入全局变量，便于使用
    g.user = result

    return True
