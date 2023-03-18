from flask import Flask

app = Flask(__name__)

#Index page 
@app.route('/')
def index():
    return '<h1>Student Management API</h1>'
