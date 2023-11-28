#!/bin/bash
"sudo yum install httpd -y"
"wget https://www.free-css.com/assets/files/free-css-templates/download/page296/klinik.zip"
"sudo unzip klinik.zip"
"sudo mv ./clinic-website-template /var/www/html/"
"sudo systemctl enable httpd"
"sudo systemctl start httpd"
