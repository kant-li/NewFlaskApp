-- 新增数据库 --
CREATE DATABASE IF NOT EXISTS flask_app;
CREATE DATABASE IF NOT EXISTS flask_app_test;

-- 新增用户和数据库，赋予对应权限 --
CREATE USER IF NOT EXISTS 'flask_app'@'localhost' IDENTIFIED BY 'flask_app-password';
GRANT ALL ON flask_app.* TO 'flask_app'@'localhost';
GRANT ALL ON flask_app_test.* TO 'flask_app'@'localhost';
