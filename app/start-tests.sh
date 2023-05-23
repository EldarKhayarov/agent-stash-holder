#! /usr/bin/env sh


export DATABASE_DSN="postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${DB_HOST}/${POSTGRES_DB}"
alembic upgrade head
pytest --rootdir=/app/tests
