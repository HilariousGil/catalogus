FROM python:2.7-wheezy
MAINTAINER datapunt.ois@amsterdam.nl

EXPOSE 8100

# Apt-ing
RUN apt-get update \
	&& apt-get install -y \
		postgresql \
		libpq-dev \
		git-core \
		solr-jetty \
		redis-server \
		vim \
		sudo \
	&& apt-get clean \
	&& pip install --upgrade pip

# Adding user
RUN adduser --system ckan

# Installing UWSGI en CKAN
RUN pip install uwsgi
RUN pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.6.0#egg=ckan'
# Installing CKAN dependencies
RUN pip install -r /src/ckan/requirements.txt

# Installing other requirements
# RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /etc/ckan/default \
	&& mkdir /home/ckan/etc \
	&& chown -R ckan /etc/ckan 

# Setting up jetty and solr
COPY ckan/jetty /etc/default/jetty
RUN mv /etc/solr/conf/schema.xml /etc/solr/conf/schema.xml.bak \
	&& ln -s /src/ckan/ckan/config/solr/schema.xml /etc/solr/conf/schema.xml
#	&& service jetty start

# Setting ckan app
# USER ckan
# Set the code in the right place
COPY ckan /app/

