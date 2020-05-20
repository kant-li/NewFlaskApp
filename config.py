"""
获取配置
"""
import os
import dotenv

env_path = os.path.join(os.path.dirname(__file__), ".env")
dotenv.load_dotenv(env_path)


class BasicConfig:
    # mysql
    MYSQL_ADDRESS = os.environ.get("MYSQL_ADDRESS", "127.0.0.1")
    MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
    MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "sandbox")
    MYSQL_DATABASE_TEST = os.environ.get("MYSQL_DATABASE", "sandbox-test")
    MYSQL_USER = os.environ.get("MYSQL_USER", "sandbox")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        + MYSQL_USER
        + ":"
        + MYSQL_PASSWORD
        + "@"
        + MYSQL_ADDRESS
        + ":"
        + str(MYSQL_PORT)
        + "/"
        + MYSQL_DATABASE
    )
    SQLALCHEMY_DATABASE_URI_TEST = (
            "mysql://"
            + MYSQL_USER
            + ":"
            + MYSQL_PASSWORD
            + "@"
            + MYSQL_ADDRESS
            + ":"
            + str(MYSQL_PORT)
            + "/"
            + MYSQL_DATABASE_TEST
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    REDIS_ADDRESS = os.environ.get("REDIS_ADDRESS", "127.0.0.1")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
    REDIS_URL = os.environ.get(
        "REDIS_URL", "redis://" + REDIS_ADDRESS + ":" + str(REDIS_PORT)
    )

    # swagger
    SWAGGER_TITLE = "Taraxa Sandbox"

    # email
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 465))
    MAIL_USE_SSL = bool(os.environ.get('MAIL_USE_SSL', True))
    MAIL_USE_TLS = bool(os.environ.get('MAIL_USE_TLS', False))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', MAIL_USERNAME)

    # 服务器
    HTTP_HOST = "127.0.0.1"
    HTTP_PORT = 5000

    # 其它
    SECRET_KEY = os.environ.get("SECRET_KEY", "sandbox")
    TOKEN_EXPIRATION = int(os.environ.get("EXPIRATION", 60*60*24*30))


config = BasicConfig()
