-- 新增数据库 --
CREATE DATABASE IF NOT EXISTS sandbox;
CREATE DATABASE IF NOT EXISTS sandbox-test;

-- 新增用户和数据库，赋予对应权限 --
CREATE USER IF NOT EXISTS 'sandbox'@'localhost' IDENTIFIED BY 'sandbox-password';
GRANT ALL ON sandbox.* TO 'sandbox'@'localhost';
GRANT ALL ON sandbox-test.* TO 'sandbox'@'localhost';
