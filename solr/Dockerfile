FROM solr:6.3

USER root
RUN apt-get update \
	&& apt-get install -y \
		libpq-dev \
		git-core \
		vim \
		sudo \
		python-dev \
		python-pip \
		python-virtualenv \
	&& apt-get clean \
	&& pip install --upgrade pip

RUN pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.6.0#egg=ckan'

RUN ln -s /src/ckan/ckan/config/solr/schema.xml /opt/solr/schema.xml

WORKDIR /opt/solr
USER $SOLR_USER

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["solr-foreground"]