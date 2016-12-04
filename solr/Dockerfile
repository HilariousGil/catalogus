FROM ubuntu:14.04

USER root
RUN apt-get update \
    && apt-get -y install wget vim sudo openjdk-7-jdk \
    && mkdir /usr/java \
    && ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default \
    && cd /opt \
    && wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz \
    && tar -xvf solr-4.7.2.tgz \
    && cp -R solr-4.7.2/example /opt/solr \
    && cd /opt/solr/solr \
    && apt-get clean \
    && mv collection1 ckan \
    && echo "name=ckan" > ckan/core.properties

WORKDIR /opt/solr
COPY schema.xml /opt/solr
COPY docker-entrypoint.sh /opt/solr
COPY schema.xml /opt/solr/solr/ckan/conf

EXPOSE 8983
USER $SOLR_USER
CMD bash /opt/solr/docker-entrypoint.sh
