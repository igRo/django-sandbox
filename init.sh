#!/bin/sh

echo creating project structure...
mkdir -p ~/web/{etc,uploads,public}/
mkdir -p ~/web/public/{img,js,css}/

echo copying and linking nginx configuration file...
cp -f $(dirname $0)/nginx.conf ~/web/etc/nginx.conf
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default

echo restarting nginx...
sudo /etc/init.d/nginx restart
