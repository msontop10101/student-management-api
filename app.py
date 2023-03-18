
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def hello_world():
    return 'Hello from Flask!'

=======
def index():
    return '<h1>Student Management API</h1>'
>>>>>>> 2d8621538a30d4b5e45c47ea4e687f38f2169fb5
