eenmalige setup DB
pg_restore -d ckan -h database_ckan -p 5432 -U ckan /data/dump.pgsql


