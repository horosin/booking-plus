#!/bin/sh
set -e

until curl http://${DATABASE_URL:-db}:${DATABASE_PORT:-5432}/ 2>&1 | grep '52'; do
  echo "Postgres is unavailable - sleeping"
  sleep 5
done

echo "Postgres is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    /venv/bin/python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    /venv/bin/python manage.py collectstatic --noinput
fi

exec "$@"