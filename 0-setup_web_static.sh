#!/usr/bin/env bash
# comment
sudo apt update
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
touch /data/web_static/shared/index.html
echo <html><head></head><body>HTML</body></html>" >> /data/web_static/shared/index.html
ln -s /data/web_static/release/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
statix="
location /hbnb_static/ {
	alias /data/web_static/current/;
	autoindex off;
	}
"
sudo sed -i "37i\ $statix" /etc/nginx/sites-enabled/default
