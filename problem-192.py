#Todo API Example

from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary database
todos = []

# get all todos
@app.route("/todos", methods=["GET"])
def get_todos():

    return jsonify(todos)

# add new todo
@app.route("/todos", methods=["POST"])
def add_todo():

    data = request.json

    todos.append(data)

    return jsonify({
        "message": "Todo added successfully",
        "todos": todos
    })

# update todo
@app.route("/todos/<int:index>", methods=["PUT"])
def update_todo(index):

    data = request.json

    if index < len(todos):

        todos[index] = data

        return jsonify({
            "message": "Todo updated",
            "todos": todos
        })

    return jsonify({
        "error": "Todo not found"
    })

# delete todo
@app.route("/todos/<int:index>", methods=["DELETE"])
def delete_todo(index):

    if index < len(todos):

        deleted = todos.pop(index)

        return jsonify({
            "message": "Todo deleted",
            "deleted": deleted
        })

    return jsonify({
        "error": "Todo not found"
    })

# run server
app.run(debug=True)

'''
output:-

Server running on:
http://127.0.0.1:5000/

GET /todos
[]

POST /todos
{
   "task":"Learn Python API"
}

Response:
{
   "message":"Todo added successfully"
}

GET /todos
[
   {
      "task":"Learn Python API"
   }
]
'''