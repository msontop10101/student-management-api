from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.users import User
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus

auth_namespace = Namespace('auth',description='Authentication Namespace')

signup_model=auth_namespace.model(
    'User', {
        'id':fields.Integer(),
        'name':fields.String(required=True,description='Name of user'),
        'email':fields.String(required=True,description='Email field'),
        'password':fields.String(required=True,description='Password field')
    }
)

@auth_namespace.route('/signup')
class Signup(Resource):

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(signup_model)
    def post(self):
        """
            Creat a new user
        """
        data=request.get_json()
        new_user=User(
            name=data.get('name'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))
        )

        new_user.save()

        return new_user, HTTPStatus.CREATED

@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Generate a JWT pair
        """
        pass
