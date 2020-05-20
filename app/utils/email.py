"""
send email
"""

from flask_mail import Message
from app.app import mail


def send_mail(subject, recipients, body=""):
    """发送邮件"""
    message = Message(subject=subject, recipients=recipients, body=body)
    mail.send(message)


####
# 应用函数
####
def send_verification_code_by_email(recipient: str, code: str = ""):
    """发送验证码"""
    body = "Your verification code is " + code
    send_mail("Verification code from SandBox", recipients=[recipient], body=body)
