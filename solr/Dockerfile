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

WORKDIR /opt/solr
COPY schema.xml /opt/solr
USER $SOLR_USER

# ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["solr-foreground"]
