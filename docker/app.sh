#!/bin/bash

alembic upgrade head

python src/commands/add_data_for_DB.py

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000