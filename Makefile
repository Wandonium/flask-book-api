build: 
	docker build -t wandonium/flask-book-api .

run: 
	docker run --name flask-book-api -d -p 8000:5000 --rm wandonium/flask-book-api:latest

build-prod:
	docker build -t wandonium/flask-book-api .
	docker push wandonium/flask-book-api:latest