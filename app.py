from flask import Flask

app = Flask(__name__)

#Index page 
@app.route('/')
def index():
    return '<h1>Student Management API</h1>'

@app.route('/students')
def students():
    return '<h1>List of students</h1>'