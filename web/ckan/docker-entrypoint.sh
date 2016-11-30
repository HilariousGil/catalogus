#!/usr/bin/env bash
echo Building db

cd /src/ckan
#paster db init -c /app/config.ini
#paster db upgrade -c /app/config.ini
paster serve /app/config.ini
