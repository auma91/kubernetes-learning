from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = '192.168.1.128'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Myworkfoo12'
app.config['MYSQL_DB'] = 'db_todo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
CORS(app)

@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
	cur = mysql.connection.cursor()
	cur.execute("Select * from db_todo.tasks")
	rv = cur.fetchall()
	print(jsonify(rv))
	return jsonify(rv)

@app.route('/api/task', methods=['POST'])
def add_task():
	cur = mysql.connection.cursor()
	title = request.get_json()['title']
	cur.execute("INSERT INTO db_todo.tasks (title) VALUES ('" + str(title) + "')")
	mysql.connection.commit()
	result = {'title':title}
	
	return jsonify({"result":result})

@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
	cur = mysql.connection.cursor()
	title = request.get_json()['title']
	
	cur.execute("UPDATE db_todo.tasks SET title = '" + str(title) + "' WHERE id = " + id)
	
	result = {"title":title}
	return jsonify({"result":result})

@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
	cur = mysql.connection.cursor()
	response = cur.execute("DELETE FROM db_todo.tasks WHERE id = " + id)
	mysql.connection.commit()
	
	if response > 0:
		result = {'message' : 'record deleted'}
	else:
		result = {'message' : 'no record found'}
		
	return jsonify({'result':result})

if  __name__  == "__main__":
	app.run(debug=True)
