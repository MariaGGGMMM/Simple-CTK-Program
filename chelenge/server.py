from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, User!</p>"

@app.route("/profile")
def profile():                          
    return "name : Maria"

@app.route("/add_post", methods=['POST'])
def add_post():
    #...
    return "Success"

@app.route("/add_cat", methods=['POST'])
def add_cat():
    #...
    return "Success"


