"""
user model
"""

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

from config import config
from app.app import db

TOKEN_SERIALIZER = Serializer(config.SECRET_KEY, config.TOKEN_EXPIRATION)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), default="")
    email = db.Column(db.String(64), default="", unique=True)
    password_hash = db.Column(db.String(256), default="")

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    def generate_auth_token(self):
        """生成token"""
        return TOKEN_SERIALIZER.dumps({"id": self.id}).decode('utf8')

    @classmethod
    def verify_auth_token(cls, token):
        """验证token"""
        try:
            data = TOKEN_SERIALIZER.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data.get('id', 0))
        return user

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    def save(self) -> int:
        """保存到数据库"""
        db.session.add(self)
        db.session.commit()
        return self.id
