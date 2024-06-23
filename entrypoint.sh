#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
sleep 0.1
done

echo "PostgreSQL started"

echo "Wainting for elasticsearch..."

while ! nc -z $ELASTIC_HOST $ELASTIC_PORT; do
    sleep 0.1
done

echo "Elasticsearch started"

# python ./app/manage.py flush --no-input
python ./app/manage.py migrate --no-input
python ./app/manage.py search_index --rebuild -f
python ./app/manage.py collectstatic --no-input
# python ./app/manage.py loaddata ./db.json
# python ./app/manage.py shell < ./config/create_superuser.py
echo "РАЗ ДВА ТРИ"
python /src/app/manage.py runserver 0.0.0.0:8000
# exec "$@"