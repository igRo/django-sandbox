#!/bin/sh

echo creating project structure...
mkdir -p ~/web/{etc,uploads,public}/
mkdir -p ~/web/public/{img,js,css}/

echo moving and linking nginx configuration file...
mv ./nginx.conf ~/web/etc/nginx.conf
sudo ln -sf ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/default

echo restarting nginx...
sudo /etc/init.d/nginx restart
