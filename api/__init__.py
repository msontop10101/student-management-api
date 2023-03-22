from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .students.views import students_namespace
from .courses.views import courses_namespace

def create_app():
    app=Flask(__name__)

    api=Api(app)

    api.add_namespace(auth_namespace,path='/auth')
    api.add_namespace(students_namespace,path='/students')
    api.add_namespace(courses_namespace,path='/courses')

    return app