FROM ubuntu:16.04
MAINTAINER datapunt.ois@amsterdam.nl

EXPOSE 5000

# Preventing frontend error
RUN export DEBIAN_FRONTEND="noninteractive"
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
		netcat-openbsd \
        curl \
	&& apt-get clean \
	&& pip install --upgrade pip

# Adding user
RUN adduser --system ckan

# Installing UWSGI en CKAN
RUN pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.6.0#egg=ckan'
# Installing CKAN dependencies

# Inject setuptools 20.4 to prevent exception
RUN sed -i '1s/^/setuptools==20.4 /' /src/ckan/requirements.txt

RUN pip install -r /src/ckan/requirements.txt
RUN mkdir -p /etc/ckan/default \
	&& mkdir /home/ckan/etc \
	&& mkdir /var/lib/ckan \
	&& chown -R ckan /etc/ckan /var/lib/ckan

# Setting ckan app
USER ckan
COPY ckan /app/
RUN export CKAN_INI=/app/config.ini

CMD /app/docker-entrypoint.sh
