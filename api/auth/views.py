from flask_restx import Namespace, Resource

auth_namespace = Namespace('auth',description='Authentication Namespace')

@auth_namespace.route('/')
class HelloAuth(Resource):

    def get(self):
        return {"message":"Hello Auth."}