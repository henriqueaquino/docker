FROM debian 

RUN apt-get update

RUN apt-get install -y \
	 python \
	apache2 \
	net-tools \
	sysstat 

RUN apt-get update

RUN mkdir /home/service/ \
	&& mkdir /var/log/service/ \
	&& chmod 755 /home \
	&& chmod 755 /home/service \ 
	&& chmod 777 /var/log/service/

COPY ./configurations/service-files/set-stats /home/service/

RUN chmod 755 /home/service/set-stats 

COPY ./configurations/service-files/mya2.conf /etc/apache2/conf-available

RUN mkdir /var/www/py/

COPY ./configurations/py/*.py /var/www/py/ 

RUN chmod 755 /var/www/py/*.py && a2enconf mya2.conf 

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
