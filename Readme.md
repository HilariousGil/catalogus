eenmalige setup DB
paster db init -c /app/config.ini
paster db upgrade -c /app/config.ini
pg_restore -d ckan -h database_ckan -p 5432 -U ckan /data/dump.pgsql


