"""
api for users
"""

from flask import Blueprint, request
from flasgger import swag_from

from app.models.user import User
from app.utils.utils import (
    successful_response,
    error_response,
    valid_email_address,
    generate_verification_code,
)
from app.utils.email import send_verification_code_by_email
from app.utils.redis import redis_add_str, redis_get_str
from app.utils.auth import auth

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/send_verification_code", methods=["GET"])
@swag_from("swagger_files/user/send_verification_code.yaml")
def send_verification_code():
    """发送邮箱验证码"""
    # 验证是合法邮箱
    email = request.args.get("email")
    if (not email) or (not valid_email_address(email)):
        return error_response(message="Invalid email address.")

    # 生成并发送验证码
    verification_code = generate_verification_code()
    redis_add_str(name=email, value=verification_code, ex=60 * 30)
    send_verification_code_by_email(recipient=email, code=verification_code)

    return successful_response(
        message="A verification code has been sent to your email. Expire in 30 minutes."
    )


@user.route("/register", methods=["POST"])
@swag_from("swagger_files/user/register.yaml")
def register():
    """注册"""
    # 验证用户是否已存在
    email = request.values.get("email", "")
    _user = User.query.filter_by(email=email).first()
    if _user is not None:
        return error_response(message="This email has registered.")

    # 确定验证码是否有效
    verification_code = request.values.get("verification_code", "")
    if verification_code != redis_get_str(email):
        return error_response(message="Invalid verification code.")

    # 新增用户
    password = request.values.get("password", "").strip()
    username = request.values.get("username", "").strip()
    if (not password) or (not username):
        return error_response(message="Invalid password.")

    new_user = User(email=email, username=username, password=password)
    new_user.save()

    # 生成 token 并返回
    token = new_user.generate_auth_token()

    return successful_response(data={"token": token})


@user.route("/login", methods=["POST"])
@swag_from("swagger_files/user/login.yaml")
def login():
    """登录"""
    # 验证密码
    email = request.values.get("email", "").strip()
    _user = User.query.filter_by(email=email).first()
    if not _user:
        return error_response(message="User not exists.")

    password = request.values.get("password", "").strip()
    if not _user.check_password(password):
        return error_response(message="Invalid email or password.")

    # 生成 token 并返回
    token = _user.generate_auth_token()

    return successful_response(data={"token": token})


@user.route("/token_test", methods=["GET"])
@auth.login_required
def token_test():
    """测试token使用"""
    return successful_response(message="token verified")
