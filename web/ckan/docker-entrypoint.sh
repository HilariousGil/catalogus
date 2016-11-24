echo Building db

chown ckan: /var/lib/ckan

cd /src/ckan
paster db init -c /app/config.ini

cd /src/ckan
paster serve /app/config.ini
