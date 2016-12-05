#!/usr/bin/env bash

set -u
set -e

# wait for postgres to be started
while ! netcat -z "database_ckan" "5432"
do
	echo "Waiting for solr..."
	sleep 1
done

# wait for solr to be started
while ! netcat -z "solr_ckan" "8983"
do
	echo "Waiting for solr..."
	sleep 1
done

echo Building db

cd /src/ckan

# rebuild solr index
#paster search-index rebuild -c /app/config.ini
paster db init -c /app/config.ini
paster serve /app/config.ini
