import sqlite3
from task import Task
import json

# conn = sqlite3.connect('task .db')
conn = sqlite3.connect(':memory:', check_same_thread=False)

c = conn.cursor()

c.execute("""CREATE TABLE tasks (
			id integer,
			title text,
			description text,
			done integer
			)""")


def insertTask(task):
	with conn:
		c.execute("INSERT INTO tasks VALUES (:id, :title, :description, :done)", {
		          'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done})
		c.execute("SELECT * FROM tasks WHERE id = :id", {'id': task.id})
	return jsonConversionForSingle(c.fetchall()[0])


def getTaskByID(id):
	c.execute("SELECT * FROM tasks WHERE id = :id", {'id': id})
	taskDB = c.fetchall()
	print(taskDB, "DB")
	print(len(taskDB), 'count')
	if len(taskDB) == 0:
		return {'task':"No Task Found"}
	return jsonConversionForSingle(taskDB[0])


def getAllTasks():
	c.execute("SELECT * FROM tasks")
	return jsonConversionForMulti(c.fetchall())


def updateTask(title, description, done, id):
	c.execute('''UPDATE tasks SET title = :title, description = :description, done = :done
		WHERE id = :id''',
		{'title': title, 'description': description, 'done': done, 'id': id})
	c.execute("SELECT * FROM tasks WHERE id = :id", {'id': id})
	return jsonConversionForSingle(c.fetchall()[0])


def removeTask(id):
	with conn:
		c.execute("DELETE from tasks WHERE id = :id",
			{'id': id})
		return {"isSuccess":True}


def jsonConversionForSingle(taskFromDB):
	task = {
	    'id': taskFromDB[0],
	    'title': taskFromDB[1],
	    'description': taskFromDB[2],
	    'done': taskFromDB[3]
	}
	jsonStr = json.dumps(task)
	return json.loads(jsonStr)


def jsonConversionForMulti(tasksFromDB):
	arrTask = []
	for taskDB in tasksFromDB:	
		task = {
		    'id': taskDB[0],
		    'title': taskDB[1],
		    'description': taskDB[2],
		    'done': taskDB[3]
		}
		arrTask.append(task)
	jsonStr = json.dumps(arrTask)
	return json.loads(jsonStr)

taskOne = Task(55,'jitsadfu','sadfads guy', 1)
taskTwo = Task(55,'sdfasdfadsf','564564 guy', 1)

c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)", (taskOne.id, taskOne.title, taskOne.description, taskOne.done))
conn.commit()

# c.execute("INSERT INTO tasks VALUES (:id, :title, :description, :done)", {'id':taskTwo.id, 'title':taskTwo.title, 'description':taskTwo.description, 'done':taskTwo.done})
# conn.commit()


# c.execute("SELECT * FROM tasks WHERE id = ?", (1,))

# print(c.fetchall())

print(getTaskByID(55))

# c.execute("SELECT * FROM tasks WHERE id = :id", {'id':55})
# taskFromDB = c.fetchall()[0]
# print(jsonConversion(taskFromDB))

conn.commit()
# conn.close()
