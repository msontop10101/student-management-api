from flask_restx import Namespace, Resource

students_namespace = Namespace('students',description='Students Namespace')

@students_namespace.route('/')
class HelloStudents(Resource):

    def get(self):
        return {"message":"Hello Students."}