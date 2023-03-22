from flask_restx import Namespace, Resource

students_namespace = Namespace('students',description='Students Namespace')

@students_namespace.route('/students')
class StudentsGetCreate(Resource):
    def get(self):
        """
        Get all students
        """

        pass

    def post(self):
        """
        Add a new student
        """

        pass

@students_namespace.route('/student/<int:student_id>')
class GetUpdateDelete(Resource):
    
    def get(self, student_id):
        """
            Get a student by id
        """
        pass

    def put(self, student_id):
        """
            Update a student by id 
        """

        pass

    def delete(self, student_id):
        """
            Delete a student by id
        """
        pass