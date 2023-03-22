from flask_restx import Namespace, Resource

courses_namespace = Namespace('courses',description='Students Namespace')

@courses_namespace.route('/')
class HelloCourse(Resource):

    def get(self):
        return {"message":"Hello Courses."}