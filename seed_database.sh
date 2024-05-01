#!/bin/bash

rm db.sqlite3
rm -rf ./LucidJournalapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations LucidJournalapi
python3 manage.py migrate LucidJournalapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata remcount
python3 manage.py loaddata factors
python3 manage.py loaddata wakemethod
python3 manage.py loaddata entries
