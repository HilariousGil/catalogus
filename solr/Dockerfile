FROM solr:6.3

USER root
RUN apt-get update \
	&& apt-get install -y \
		git-core \
		vim \
		sudo \
	&& apt-get clean # \

WORKDIR /opt/solr
COPY schema.xml /opt/solr
COPY schema.xml /opt/solr/server/solr/mycores/mycore/conf
USER $SOLR_USER
CMD ["solr-foreground"]
