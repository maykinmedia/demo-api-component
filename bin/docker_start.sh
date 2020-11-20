#!/bin/sh

set -e

# Apply database migrations
>&2 echo "Apply database migrations"
python src/manage.py migrate

# Start server
>&2 echo "Starting server"
uwsgi \
    --http :8000 \
    --module demo_api.wsgi \
    --static-map /static=/app/static \
    --static-map /media=/app/media  \
    --chdir src \
    --processes 2 \
    --threads 2
    # processes & threads are needed for concurrency without nginx sitting inbetween
