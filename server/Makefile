build-database:
	cd database && \
	docker build . -t nodeapp

build-analyzer:
	cd sentiment_analyzer && \
	docker build . -t sentiment-analyzer

build-dealership:
	docker build . -t dealership

build: build-database build-analyzer build-dealership

run-backend:
	python manage.py runserver 0.0.0.0:8001

compose-up:
	docker-compose up -d

compose-down:
	docker-compose down