from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource, Api
import dbManager
from task import Task
import sqlite3

app = Flask(__name__)
api = Api(app)


class GetAllTask(Resource):
    def get(self):
        tasks = dbManager.getAllTasks()
        return jsonify({'allTask': tasks})

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}


class GetTask(Resource):
    def get(self, taskID):
    	task = dbManager.getTaskByID(taskID)
    	if "task" in task:
    		return {"error": task["task"]}, 404
    	return jsonify({'task': task})
        


class CreateTask(Resource):
    def post(self):
        if not request.get_json() or not 'title' in request.get_json():
            return {"error": "bad request paramter."}, 404
        taskToInsert = Task(request.json.get('id', "Default"), request.json.get(
            'title', "Default"), request.json.get('description', "Default"), 1)
        task = dbManager.insertTask(taskToInsert)
        return jsonify({'task': task})


class UpdateTask(Resource):
    def put(self, taskID):
        if not request.get_json():
            return {"error": "bad request, json not in correct formate."}, 400
        if 'title' in request.get_json() and type(request.get_json()['title']) != str:
            return {"error": "bad request paramter, title."}, 400
        if 'description' in request.get_json() and type(request.get_json()['description']) is not str:
            return {"error": "bad request paramter, description"}, 404
        if 'done' in request.get_json() and type(request.get_json()['done']) is not bool:
            return {"error": "bad request paramter, done"}, 400
        taskTitle = request.json.get('title','title')
        taskDescription = request.json.get('description','description')
        taskDone = request.json.get('done', False)
        task = dbManager.updateTask(taskTitle, taskDescription, taskDone, taskID)
        return jsonify({'task': task})

class DeleteTask(Resource):
    def delete(self, taskID):
    	return jsonify({'result': dbManager.removeTask(taskID)})


api.add_resource(GetAllTask, '/allTask/')
api.add_resource(GetTask, '/taskID/<int:taskID>')
api.add_resource(CreateTask, '/addNewTask/')
api.add_resource(UpdateTask, '/updateTask/<int:taskID>')
api.add_resource(DeleteTask, '/deleteTask/<int:taskID>')

if __name__ == '__name__':
    app.run(debug=True)
