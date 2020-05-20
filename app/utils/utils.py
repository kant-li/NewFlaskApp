"""
some basic utils functions
"""
from typing import Dict
import re
import random

from flask import make_response, jsonify

EMAIL_REGEX = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")


def successful_response(status: int = 200, message: str = "success", data: Dict = None):
    """成功返回"""
    if not data:
        data = {}
    return make_response(
        jsonify({"status": status, "message": message, "data": data}), status
    )


def error_response(status: int = 400, message: str = "error", data: Dict = None):
    """错误返回"""
    if not data:
        data = {}
    return make_response(
        jsonify({"status": status, "message": message, "data": data}), status
    )


def valid_email_address(email: str = "") -> bool:
    """验证邮箱地址是否有效"""
    try:
        return EMAIL_REGEX.match(email) is not None
    except TypeError:
        pass
    return False


def generate_verification_code():
    """生成验证码"""
    return str(random.randint(1, 9)) + "".join(
        [str(random.randint(0, 9)) for i in range(5)]
    )
