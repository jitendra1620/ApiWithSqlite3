from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource, Api
import dbManager

app = Flask(__name__)
api = Api(app)



class GetAllTask(Resource):
    def get(self):
        return jsonify({'allTask': dbManager.getAllTasks()})

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}


# class GetTask(Resource):
#     def get(self, taskID):
#         taskToSend = None
#         for task in tasks:
#             if task['id'] == taskID:
#                 taskToSend = task
#                 return jsonify({'task': task})
#         if taskToSend == None:
#             return {"message": "Contact does not exist."}, 404


# class CreateTask(Resource):
#     def post(self):
#         if not request.get_json() or not 'title' in request.get_json():
#             return {"error": "bad request paramter."}, 404
#         task = {
#             'id': tasks[-1]['id'] + 1,
#             'title': request.json['title'],
#             'description': request.json.get('description', ""),
#             'done': False
#         }
#         tasks.append(task)
#         return jsonify({'task': task})


# class UpdateTask(Resource):
#     def put(self, taskID):
#         task = [task for task in tasks if task['id'] == taskID]
#         if len(task) == 0:
#             return {"error": "bad request paramter."}, 400
#         if not request.get_json():
#             return {"error": "bad request, json not in correct formate."}, 400
#         if 'title' in request.get_json() and type(request.get_json()['title']) != str:
#             return {"error": "bad request paramter, title."}, 400
#         if 'description' in request.get_json() and type(request.get_json()['description']) is not str:
#             return {"error": "bad request paramter, description"}, 404
#         if 'done' in request.get_json() and type(request.get_json()['done']) is not bool:
#             return {"error": "bad request paramter, done"}, 400
#         task[0]['title'] = request.json.get('title', task[0]['title'])
#         task[0]['description'] = request.json.get('description', task[0]['description'])
#         task[0]['done'] = request.json.get('done', task[0]['done'])
#         return jsonify({'task': task[0]})

# class DeleteTask(Resource):
# 	def dele(self, taskID):
# 		task = [task for task in tasks if task['id'] == taskID]
#         if len(task) == 0:
#             return {"error": "bad request paramter."}, 400
#         tasks.remove(task[0])
#     return jsonify({'result': True})
		
api.add_resource(GetAllTask, '/allTask/')
# api.add_resource(GetTask, '/taskID/<int:taskID>')
# api.add_resource(CreateTask, '/addNewTask/')
# api.add_resource(UpdateTask, '/updateTask/<int:taskID>')
# api.add_resource(DeleteTask, '/deleteTask/<int:taskID>')

if __name__ == '__name__':
    app.run(debug=True)
