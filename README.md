# User Data Library

## Project Description
This project is a demonstration of a RESTful API built with Python Flask and SQLLite, deployed using Docker and Kubernetes. The API allows users to perform CRUD operations on a sample dataset.

## Technologies Used
- Python
- Flask
- SQLite
- Docker
- Kubernetes
- REST API

## Installation

To deploy the application locally using Docker, follow these steps:
1. Clone this repository: `git clone https://github.com/saiful1984/techtest.git`
2. Ensure docker is installed in the system.
3. Run the Docker compose:

    `docker-compose build`
    
    `docker-compose up`

To deploy the application on a Kubernetes cluster, follow these steps:
1. Make sure you have a Kubernetes cluster configured and `kubectl` installed.
2. Apply the Kubernetes deployment manifest: `kubectl apply -f kubernetes/deployment.yaml`
3. Apply the Kubernetes service manifest: `kubectl apply -f kubernetes/service.yaml`
4. Apply the Kubernetes configmap manifest: `kubectl apply -f kubernetes/configmap.yaml`

To deploy the application on a Kubernetes cluster using helm chart, run the below command:

`helm install userdb-helm userdb-helm --values ./userdb-helm/values.yaml`

## Usage

Once the application is deployed, the REST API will be published at http://localhost:8000/api/v1.0/apiTasks/ in your system.
You can interact with the RESTful API using tools like [Postman](https://www.postman.com/) or `curl`.
- GET `http://localhost:8000/api/v1.0/apiTasks`: Retrieve all resources
- GET `http://localhost:8000/api/v1.0/apiTasks/{id}`: Retrieve a specific resource by ID
- POST `http://localhost:8000/api/v1.0/apiTasks/{id}?firstName=syed&middelName=saiful&lastName=arefin&age=29`: Create a new resource
- PUT `http://localhost:8000/api/v1.0/apiTasks/{id}?firstName=syed&middelName=saiful&lastName=arefin&age=29`: Update an existing resource
- DELETE `http://localhost:8000/api/v1.0/apiTasks/{id}`: Delete a resource by ID

Below are the sample RESTful API calls:

POST: http://localhost:8000/api/v1.0/apiTasks/1?firstName=syed&middelName=saiful&lastName=arefin&age=37

GET: http://localhost:8000/api/v1.0/apiTasks/1

POST: http://localhost:8000/api/v1.0/apiTasks/1?firstName=syed&middelName=saiful&lastName=arefin&age=20

DELETE: http://localhost:8000/api/v1.0/apiTasks/1

You can trigger the python test_app.py script to run the entire set of REST API calls. 

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is for personal use only and does not have a specific license.
