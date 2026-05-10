#Build REST API Example

from flask import Flask, jsonify

app = Flask(__name__)

# sample route
@app.route("/")

def home():
    return "Welcome to REST API"

# API route
@app.route("/student")

def student():

    data = {
        "name": "Robin",
        "age": 22,
        "department": "CSE"
    }

    return jsonify(data)

# run server
app.run(debug=True)

'''
output:-

Running on http://127.0.0.1:5000/

Open browser:

http://127.0.0.1:5000/

Output:
Welcome to REST API

http://127.0.0.1:5000/student

Output:
{
   "name":"Robin",
   "age":22,
   "department":"CSE"
}
'''