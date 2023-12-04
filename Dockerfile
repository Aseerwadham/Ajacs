FROM ubuntu/apache2
LABEL author="asee" 
RUN apt install unzip -y && mkdir deploy && cd deploy
ADD https://www.free-css.com/assets/files/free-css-templates/download/page296/little-fashion.zip .
WORKDIR deploy
RUN unzip little-fashion.zip && cp -rf 2127_little_fashion /var/www/html,
CMD [ "systemctl", "enable", "apache2.service" ]
