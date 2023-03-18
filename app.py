from flask import Flask

app = Flask(__name__)

#Index page 
@app.route('/')
def index():
    return '<h1>Student_Management_API</h1>'

@app.route('/students')
def students():
    return '<h1>List_of_students</h1>'