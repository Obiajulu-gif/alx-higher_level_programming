-- script that lists all the privilegde of mySql user
echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
echo "CREATE USER 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
echo "SHOW GRANTS FOR 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
echo "SHOW GRANTS FOR 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
