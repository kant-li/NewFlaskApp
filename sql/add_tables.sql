-- 选择数据库 --
USE flask_app;

-- user 表 --
CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(64) NOT NULL DEFAULT '',
    password_hash VARCHAR(256) NOT NULL DEFAULT '',
    email VARCHAR(64) NOT NULL DEFAULT '',
    PRIMARY KEY (id)
);

CREATE INDEX user_username ON user(username);
CREATE INDEX user_email ON user(email);

-- 赋权 --
GRANT ALL ON sandbox.* TO 'flask_app'@'localhost';