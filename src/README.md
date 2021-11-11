Basic User data library

Basic User data library creates user data(firstname, middlename, lastname and age) in database through a build it restapi.
This mini app is created with Flask and sqlite

Installation

Go to docker-compose-yaml location.
Run docker-compose build
Run docker-compose up

Usage

The restapi will be published in http://localhost:8000/api/v1.0/apiTasks/ in your system.
Trigger "python test_app.py" to run the entire set of restapi calls.
Below restapi calls can be send.
1. POST: http://localhost:8000/api/v1.0/apiTasks/1?firstName=syed&middelName=saiful&lastName=arefin&age=37
2. GET: http://localhost:8000/api/v1.0/apiTasks/1
3. POST: http://localhost:8000/api/v1.0/apiTasks/1?firstName=syed&middelName=saiful&lastName=arefin&age=20
4. DELETE: http://localhost:8000/api/v1.0/apiTasks/1
