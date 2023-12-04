FROM ubuntu:latest

LABEL author="asee"

RUN apt-get update && \
    apt-get install -y apache2 wget unzip
RUN mkdir /deploy
WORKDIR /deploy
RUN wget https://www.free-css.com/assets/files/free-css-templates/download/page296/little-fashion.zip
RUN unzip little-fashion.zip && \
    cp -rf 2127_little_fashion/* /var/www/html/ && \
    rm -r 2127_little_fashion
WORKDIR /var/www/html
CMD ["apache2ctl", "-D", "FOREGROUND"]