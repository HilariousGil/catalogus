FROM ubuntu:16.04
MAINTAINER datapunt.ois@amsterdam.nl

EXPOSE 5000

# Preventing frontend error
RUN export DEBIAN_FRONTEND="noninteractive"
# export CKAN_SQLALCHEMY_URL="postgresql://ckan:insecure@database_ckan/ckan"
# Apt-ing
RUN apt-get update \
	&& apt-get install -y \
		postgresql \
		libpq-dev \
		git-core \
		redis-server \
		vim \
		sudo \
		python-dev \
		python-pip \
		python-virtualenv \
	&& apt-get clean \
	&& pip install --upgrade pip

# Adding user
RUN adduser --system ckan

# Installing UWSGI en CKAN
RUN pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.6.0#egg=ckan'
# Installing CKAN dependencies
RUN pip install -r /src/ckan/requirements.txt
RUN pip install uwsgi

# Installing other requirements
# RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /etc/ckan/default \
	&& mkdir /home/ckan/etc \
	&& chown -R ckan /etc/ckan 

# Setting ckan app
USER ckan
COPY ckan /app/

#CMD /app/docker-entrypoint.sh