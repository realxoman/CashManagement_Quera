.PHONY: lint
lint:
	flake8 --config=.flake8

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: run
run:
	python manage.py runserver


.PHONY: test
test:
	python manage.py test

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .coverage .cache .pytest_cache
