from flask import Flask, request
import db
import db_func


app = Flask(__name__)

@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()

    website = data['website']
    email = data['email']
    password = data['password']

    db_func.insert(db.cursor, db.connection, email, website, password)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/denis")
def hello_denis():
    return "Hello, Denis!"

@app.route("/bla")
def hello_bla():
    return "bla bla bla bla bla bla bla bla bla bla"

@app.route("/kookoo")
def hello_kookoo():
    return "you are kookoo"

@app.route("/nooo")
def hello_nooo():
    return "that isnt your buisness!"


@app.route("/yes")
def hello_yes():
    return "you are going on the weekends!"

@app.route("/add", methods =['POST'])
def add_user():
    print(request.json)


