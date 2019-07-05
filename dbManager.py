import sqlite3
import json
from task import Task

# conn = sqlite3.connect('task .db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE tasks (
			id integer,
			title text,
			description text,
			done integer
			)""")

def insertTask(task):
	with conn:
		c.execute("INSERT INTO tasks VALUES (:id, :title, :description, :done)", {'id':None, 'title':task.title, 'description':task.description, 'done':task.done})


def getTaskByID(id):
	c.execute("SELECT * FROM tasks WHERE id = :id", {'id':id})
	return json.dump(c.fetchall())

def getAllTasks():
	c.execute("SELECT * FROM tasks")
	return json.dump(c.fetchall())

def updateTask(task, title, description, done):
	c.execute('''UPDATE tasks SET title = :title, description = :description, done = :done
		WHERE id = :id''',
		{'title':task.title, 'description':task.description, 'done':task.done, 'id':task.id})
	c.execute("SELECT * FROM tasks WHERE id = :id", {'id':task.id})
	return json.dump(c.fetchall())


def removeTask(id):
	with conn:
		c.execute("DELETE from task WHERE id = :id",
			{'id':id})


# taskOne = Task(55,'jitsadfu','sadfads guy', 1)
# taskTwo = Task(55,'sdfasdfadsf','564564 guy', 1)

# c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)", (taskOne.id, taskOne.title, taskOne.description, taskOne.done))
# conn.commit()

# c.execute("INSERT INTO tasks VALUES (:id, :title, :description, :done)", {'id':taskTwo.id, 'title':taskTwo.title, 'description':taskTwo.description, 'done':taskTwo.done})
# conn.commit()


# c.execute("SELECT * FROM tasks WHERE id = ?", (1,))

# print(c.fetchall())


# c.execute("SELECT * FROM tasks WHERE id = :id", {'id':55})

# print(c.fetchall())

conn.commit()
conn.close()