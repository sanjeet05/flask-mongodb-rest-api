# flask-mongodb-rest-api
A simple REST Api using Flask-Restful and MongoDB, used to store task with timestamps. The Api supports `get`, `put`, `post` and `delete` functions and has multiple endpoints for more complicated `get` requests.

### start virtual env ###
```
$ source venv/bin/activate
$ deactivate
$ python3 app.py

```

### Install requirements: ###
Install the requirements in a virtual environment.
```
pip3 install -r requirements.txt
```
### API Endpoints: ###
```
@GET
http://127.0.0.1:5000/api/v1/todo/tasks
http://127.0.0.1:5000/api/v1/todo/tasks/<_id>

@POST
http://127.0.0.1:5000/api/v1/todo/tasks
BODY = {
	"title": "task 1",
	"description": "description 1"
}

@PUT
http://127.0.0.1:5000/api/v1/todo/tasks/<_id>
BODY = {
	"title": "task 2"
}

@DELETE
http://127.0.0.1:5000/api/v1/todo/tasks/<_id>

```