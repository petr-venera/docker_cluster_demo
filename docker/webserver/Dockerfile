FROM httpd:latest
MAINTAINER Petr Venera (petr.venera@seznam.cz)
COPY ./configuration/httpd.conf /usr/local/apache2/conf/httpd.conf
EXPOSE 80
CMD ["httpd", "-D", "FOREGROUND"]