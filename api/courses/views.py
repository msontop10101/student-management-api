from flask_restx import Namespace, Resource

courses_namespace = Namespace('courses',description='Students Namespace')

@courses_namespace.route('/courses')
class CoursesGetCreate(Resource):
    def get(self):
        """
        Get all courses
        """

        pass

    def post(self):
        """
        Create new course
        """

        pass

@courses_namespace.route('/orders/<int:course_id>')
class GetUpdateDelete(Resource):
    
    def get(self, course_id):
        """
            Get a course by id
        """
        pass

    def put(self, course_id):
        """
            Update a course by id 
        """

        pass

    def delete(self, course_id):
        """
            Delete a course by id
        """
        pass
