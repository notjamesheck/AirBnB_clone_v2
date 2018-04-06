#!/usr/bin/env bash
<<<<<<< HEAD
# comment
sudo apt update
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
touch /data/web_static/shared/index.html
echo <html><head></head><body>HTML</body></html>" >> /data/web_static/shared/index.html
ln -s /data/web_static/release/test /data/web_static/current
chown ubuntu /data
statix="
location /hbnb_static/ {
	alias /data/web_static/current/;
	autoindex off;
	}"
sudo sed -i "37i\ $statix"
=======
# Sets up my web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "Code: 451" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "58i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n\n" /etc/nginx/sites-enabled/default

sudo service nginx restart
>>>>>>> e14c8886cf0b87951423fd64a923f98029846c71
