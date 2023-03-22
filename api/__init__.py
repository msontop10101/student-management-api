from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .students.views import students_namespace
from .courses.views import courses_namespace
from .config.config import config_dist

def create_app(config=config_dist['dev']):
    app=Flask(__name__)

    app.config.from_object(config)
    app.config['SECRET_KEY'] = '9ee134dd8bda762b7f8f8ada41ae1eb5d19ebea4e5257df6d2bd57b300797694'

    api=Api(app)

    api.add_namespace(auth_namespace,path='/auth')
    api.add_namespace(students_namespace,path='/students')
    api.add_namespace(courses_namespace,path='/courses')

    return app