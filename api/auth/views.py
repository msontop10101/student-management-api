from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth',description='Authentication Namespace')

@auth_namespace.route('/signup')
class Signup(Resource):

    def post(self):
        """
            Creat a new user
        """
        pass

@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Generate a JWT pair
        """
        pass
