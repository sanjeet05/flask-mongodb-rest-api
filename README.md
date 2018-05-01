# flask-mongodb-rest-api
A simple REST Api using Flask-Restful and MongoDB, used to store tweets with timestamps and associated emotions. The Api supports `get`, `put`, `post` and `delete` functions and has multiple endpoints for more complicated `get` requests.



### Install requirements: ###
Install the requirements in a virtual environment.
```
pip install -r requirements.txt
```
### API: ###
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