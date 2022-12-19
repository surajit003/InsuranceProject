#!/bin/sh
if "$DATABASE" = "postgres"
then
    echo "Waiting for postgres..."
    echo "Host: $DATABASE_HOST Port: $DATABASE_PORT"
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.5
    done
    echo "PostgreSQL started"
fi

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createcachetable

exec "$@"
