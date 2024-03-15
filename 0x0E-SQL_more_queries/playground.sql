CREATE DATABASE IF NOT EXISTS `hbtn_0c_0`;
use `hbtn_0c_0`;
DROP DATABASE IF EXISTS `hbtn_0c_0`;
SHOW TABLES;

-- Creating the first table
CREATE TABLE IF NOT EXISTS first_table(`id` INT, `name`VARCHAR(256));
SHOW CREATE TABLE `first_table`;
SELECT * FROM `first_table`;
INSERT INTO `first_table` (`id`, `name`) VALUES (26062001, lower("EMMANUEL"));
SELECT COUNT(*) FROM first_table WHERE `id` = 26062001;

-- Creating the second table
use hbtn_0c_0;
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (6, "EMMANUEL", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(5, lower("EKENE"), 20);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
SELECT `score`, `name` from `second_table` ORDER BY `score` DESC;
SELECT `score`, `name` from `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
UPDATE `second_table` SET `score` = 100 WHERE `name` = upper('EMMANUEL');
DELETE FROM `second_table` WHERE `score` = 3;
SELECT AVG(`score`) AS `average` from `second_table`;
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;











-- Creating and Granting user permission
create role new_user; -- this create a user role
CREATE USER 'ekene'@'localhost' IDENTIFIED BY '26062001@Ekene'; -- create a new user and set the password
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'ekene'@'localhost' WITH GRANT OPTION; -- give limit access to a user
GRANT ALL ON *.* TO 'new_user'@'localhost' WITH GRANT OPTION; -- this give super user permission to a user

-- Revoke user permission
REVOKE CREATE, DROP ON *.* FROM 'ekene'@'localhost';

-- Drop user from the database
DROP USER 'obiajulu'@'localhost';

-- this check for all the users
select Host,User from mysql.user; 

-- show grants for a particular user
SHOW GRANTS FOR 'ekene'@'localhost';

-- restart the database
FLUSH PRIVILEGES;