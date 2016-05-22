#!/bin/sh

echo copying application files...
cp -TR $(dirname $0)/web/ ~/web/

echo creating project structure...
mkdir -p ~/web/{uploads,public}/
mkdir -p ~/web/public/{img,js,css}/

echo linking configuration files...
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf ~/web/etc/hello.conf /etc/gunicorn.d/hello
sudo ln -sf ~/web/etc/ask.conf /etc/gunicorn.d/ask

echo updating django...
sudo pip uninstall django
sudo pip3 install django

echo restarting daemons...
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql restart

echo configure mysql
mysql -uroot -p -e "CREATE DATABASE IF NOT EXISTS ask_db;"
mysql -uroot -p -e "CREATE USER 'ask_user'@'localhost' IDENTIFIED BY 'change_me';" #PASSWORD EXPIRE
mysql -uroot -p -e "GRANT ALL ON ask_db.* TO 'ask'@'localhost';"
mysql -uroot -p -e "FLUSH PRIVILEGES;"
