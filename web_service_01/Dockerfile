FROM debian 

RUN apt-get update

RUN apt-get install -y \
	 python \
	apache2	

RUN apt-get update

RUN mkdir /home/service/ \
	&& chmod 777 /home \
	&& chmod 777 /home/service 

COPY ./configurations/service_files/set_stats.sh /home/service/

RUN chmod 777 /home/service/set_stats.sh 

COPY ./configurations/service_files/mya2.conf /etc/apache2/conf-available

RUN mkdir /var/www/py/

COPY ./configurations/py/*.py /var/www/py/ 

RUN chmod 777 /var/www/py/*.py && a2enconf mya2.conf 

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
