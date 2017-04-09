# Install MySQL

sudo apt update
sudo apt install python-dev mysql-server libmysqlclient-dev

sudo pip install mysqlclient

# Config

sudo mysql_install_db
mysql -u root -p


> CREATE DATABASE quizapp CHARACTER SET UTF8;
> CREATE USER quizuser@localhost IDENTIFIED BY 'quizpassword'; //P@ssw0rD
> GRANT ALL PRIVILEGES ON quizapp.* TO quizuser@localhost;
> FLUSH PRIVILEGES;