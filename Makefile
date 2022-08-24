build-prod:
	cd app && $(MAKE) build-flask
	cd nginx && $(MAKE) build-nginx
	docker push wandonium/flask-book-api:latest
	docker push wandonium/flask-proxy:latest

run-prod:
	docker-compose -f docker-compose.prod.yml up -d