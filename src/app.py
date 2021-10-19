import flask
from flask import Flask, jsonify
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():   
  json_text = flask.jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():   
  request_body = request.data
  decoded_object = json.loads(request_body)
  todos[len(todos):] = [decoded_object]
  todos_text = flask.jsonify(todos)
  print("Incoming request with the following body", request_body)
  return todos_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    remove_todo = todos.pop(position)
    todos_text = flask.jsonify(todos)
    print("This is the position to delete: ",position)
    return todos_text
  

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)