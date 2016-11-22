service jetty8 start

echo Building db
cd /src/ckan
paster db init -c /app/config.ini

echo Linking who.ini
ln -s /src/ckan/who.ini /app/who.ini

cd /src/kcan
paster serve /app/config.ini