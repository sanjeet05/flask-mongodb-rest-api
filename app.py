from flask import Flask, jsonify, url_for, redirect, request  # For flask implementation
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from bson.objectid import ObjectId  # For ObjectId to work

app = Flask(__name__)
api = Api(app)

# mongodb config
app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
mongo = PyMongo(app)

# resource api
class TaskListAPI(Resource):

  def get(self):
    task = mongo.db.tasks
    output = []
    for s in task.find():
        output.append({'_id': str(s['_id']), 'title' : s['title'], 'description' : s['description']})
    return jsonify({'result' : output})

  def post(self):
    task = mongo.db.tasks
    title = request.json['title']
    description = request.json['description']
    task_id = task.insert({'title': title, 'description': description})
    new_task = task.find_one({'_id': task_id })
    output = {'title' : new_task['title'], 'description' : new_task['description']}
    return jsonify({'result' : output})

class TaskAPI(Resource):
    
  def get(self, task_id):
    task = mongo.db.tasks
    new_task = task.find_one({ '_id': ObjectId(task_id) })
    # print('new_task', new_task)    
    output = {'_id': str(new_task['_id']), 'title' : new_task['title'], 'description' : new_task['description']}
    return jsonify({'result' : output})

  def put(self, task_id):  
    task = mongo.db.tasks  
    title = request.json['title']
    data = {'title': title}   
    task.update({'_id': ObjectId(task_id)}, {'$set': data})
    new_task = task.find_one({'_id': ObjectId(task_id) })
    # print('new_task', new_task)   
    output = {'_id': str(new_task['_id']), 'title' : new_task['title'], 'description' : new_task['description']}
    return jsonify({'result' : output})

  def delete(self, task_id):
    mongo.db.tasks.remove({ 'id': ObjectId(task_id) })
    return jsonify({'result' : 'task has been deleted'})

# add resource to endpoints
api.add_resource(TaskListAPI, '/api/v1/todo/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/api/v1/todo/tasks/<string:task_id>', endpoint='task')

# starting point config
if __name__ == '__main__':
	app.run(debug=True)

			
