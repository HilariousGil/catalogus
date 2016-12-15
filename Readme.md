### Eenmalige setup DB

    $ pg_restore -d ckan -h database_ckan -p 5432 -U ckan /data/dump.pgsql


### Aanmaken sysadmin account

    $ paster sysadmin add <user-name> -c /app/config.ini

Je wordt daarna gevraagd een password aan te maken als deze gebruiker nog niet bestaat

