# User Data Library

## Project Description
Basic User Data Library is a Flask-based REST API that creates user data (firstname, middlename, lastname, and age) in a database. This mini application is built with Flask and SQLite.

## Technologies Used
- Python
- Flask
- SQLite
- Docker
- Kubernetes
- REST API

## Installation

### Deploy with Docker Compose

docker-compose build
docker-compose up

### Deploy with Kubernetes
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/configmap.yaml

### Deploy with Helm Charts
helm install userdb-helm userdb-helm --values ./userdb-helm/values.yaml

## Usage

The REST API will be published at http://localhost:8000/api/v1.0/apiTasks/ in your system. 
You can trigger the python test_app.py script to run the entire set of REST API calls. 
Below are the available REST API endpoints:

    POST: http://localhost:8000/api/v1.0/apiTasks/1?firstName=syed&middelName=saiful&lastName=arefin&age=37
    GET: http://localhost:8000/api/v1.0/apiTasks/1
    POST: http://localhost:8000/api/v1.0/apiTasks/1?firstName=syed&middelName=saiful&lastName=arefin&age=20
    DELETE: http://localhost:8000/api/v1.0/apiTasks/1
