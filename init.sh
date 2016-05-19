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
