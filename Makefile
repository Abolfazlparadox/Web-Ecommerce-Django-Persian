# -------------------------
# Django + React Makefile
# -------------------------

# Virtual environment
venv:
	python -m venv venv

activate:
	. venv/bin/activate  # Linux/Mac
	# venv\Scripts\activate  # Windows

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

# -------------------------
# Django project commands
# -------------------------

run:
	python manage.py runserver

shell:
	python manage.py shell

createsuperuser:
	python manage.py createsuperuser

check:
	python manage.py check

# -------------------------
# Database & Migrations
# -------------------------

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

sqlmigrate:
	python manage.py sqlmigrate $(app) $(number)

showmigrations:
	python manage.py showmigrations

flush:
	python manage.py flush --no-input

resetdb:
	python manage.py reset_db

loaddata:
	python manage.py loaddata $(fixture)

dumpdata:
	python manage.py dumpdata > data.json

# -------------------------
# Static files
# -------------------------

collectstatic:
	python manage.py collectstatic --noinput

clearcache:
	python manage.py clear_cache

# -------------------------
# Tests & Coverage
# -------------------------

test:
	python manage.py test

coverage:
	coverage run manage.py test && coverage report

# -------------------------
# Django Utilities
# -------------------------

startapp:
	python manage.py startapp $(name)

startproject:
	django-admin startproject $(name)

changepassword:
	python manage.py changepassword $(user)

dbshell:
	python manage.py dbshell

makemessages:
	python manage.py makemessages -l en

compilemessages:
	python manage.py compilemessages

# -------------------------
# React (if frontend exists)
# -------------------------

npm-install:
	cd frontend && npm install

npm-build:
	cd frontend && npm run build

npm-start:
	cd frontend && npm start

# -------------------------
# Docker (optional)
# -------------------------

docker-up:
	docker-compose up

docker-down:
	docker-compose down

docker-build:
	docker-compose build
