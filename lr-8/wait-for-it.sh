#!/usr/bin/env bash
set -e
host="$1"
shift
until pg_isready -h "$host" -U "django_user"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"
exec "$@"
