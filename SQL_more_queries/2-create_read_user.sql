-- Creates the database hbtn_0d_2 if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates the user user_0d_2 with the specified password if they don't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grants only SELECT privilege to user_0d_2 for all tables within hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Applies the privilege changes immediately
FLUSH PRIVILEGES;
