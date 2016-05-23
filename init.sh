#!/bin/sh

echo copying application files...
sudo ln -sf $(dirname $0)/web/ ~/web/

# echo creating project structure...
# mkdir -p ~/web/{uploads,public}/
# mkdir -p ~/web/public/{img,js,css}/

echo linking configuration files...
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
# sudo ln -sf ~/web/etc/hello.conf /etc/gunicorn.d/hello
sudo ln -sf ~/web/etc/ask.conf /etc/gunicorn.d/ask

echo updating django...
sudo pip uninstall django
sudo pip3 install django

echo restarting daemons...
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql restart

echo configuring mysql...
mysql -uroot -e "CREATE DATABASE IF NOT EXISTS ask_db;"

# mysql 5.7.6+
# mysql -uroot -e "CREATE USER IF NOT EXISTS 'ask_user'@'localhost' IDENTIFIED BY 'change_me';" #PASSWORD EXPIRE
# mysql -uroot -e "GRANT ALL ON ask_db.* TO 'ask_user'@'localhost';"

# mysql below 5.7.6
mysql -uroot -e "GRANT ALL ON ask_db.* TO 'ask_user'@'localhost' IDENTIFIED BY 'change_me';" #PASSWORD EXPIRE

mysql -uroot -e "FLUSH PRIVILEGES;"
