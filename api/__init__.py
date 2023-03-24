from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .students.views import students_namespace
from .courses.views import courses_namespace
from .config.config import config_dist
from .utils import db
from .models.courses import Course
from .models.students import Student
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os



def create_app(config=config_dist['dev']):
    app=Flask(__name__)

    app.config.from_object(config)
    # app.config['JWT_SECRET_KEY'] = '8e6e4a0de566d0d4dcbba1e58737cff69c9a65134c83e15df5f41ef68f7d38b0'
    app.config['SECRET_KEY'] = '9ee134dd8bda762b7f8f8ada41ae1eb5d19ebea4e5257df6d2bd57b300797694'

    os.environ['JWT_SECRET_KEY'] = '8e6e4a0de566d0d4dcbba1e58737cff69c9a65134c83e15df5f41ef68f7d38b0'
    app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

    db.init_app(app)

    migrate=Migrate(app,db)

    api=Api(app)

    api.add_namespace(auth_namespace,path='/auth')
    api.add_namespace(students_namespace,path='/students')
    api.add_namespace(courses_namespace,path='/courses')

    jwt=JWTManager(app)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Students':Student,
            'Courses':Course
        }

    return app