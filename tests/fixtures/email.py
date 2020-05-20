"""
mocker for email service
"""

from pytest import fixture


def _mock_send_email(*args, **kwargs):
    pass


@fixture
def mock_verification_code_email():
    """替换发送邮件的函数"""
    from app.apis import user

    user.send_verification_code_by_email = _mock_send_email
