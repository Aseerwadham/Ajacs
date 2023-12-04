#!/bin/bash
"sudo apt install apache2 unzip -y"
"wget https://www.free-css.com/assets/files/free-css-templates/download/page296/little-fashion.zip"
"sudo unzip little-fashion.zip"
"sudo cp -rf ./2127_little_fashion /var/www/html/"
"sudo systemctl enable apache2.service"
"sudo systemctl start apache2.service"
