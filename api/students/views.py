from flask_restx import Namespace, Resource,fields
from flask_jwt_extended import jwt_required
from ..models.students import Student
from http import HTTPStatus
from ..utils import db

students_namespace = Namespace('students',description='Students Namespace')

student_model=students_namespace.model(
    'Students', {
        'id':fields.Integer(description='An ID'),
        'full_name':fields.String(description='Full Name',required=True),
        'email':fields.String(description='Email address',required=True)
    }
)

@students_namespace.route('/students')
class StudentsGetCreate(Resource):

    @students_namespace.marshal_with(student_model)
    @jwt_required()
    def get(self):
        """
        Get all students
        """ 

        student=Student.query.all()

        return student, HTTPStatus.OK

    @students_namespace.expect(student_model)
    @students_namespace.marshal_with(student_model)
    @jwt_required()
    def post(self):
        """
        Add a new student
        """

        data=students_namespace.payload

        new_student=Student(
            full_name=data['full_name'],
            email=data['email']
        )

        new_student.save()

        return new_student, HTTPStatus.CREATED

@students_namespace.route('/student/<int:student_id>')
class GetUpdateDelete(Resource):
    
    @students_namespace.marshal_with(student_model)
    def get(self, student_id):
        """
            Get a student by id
        """
        student=Student.get_by_id(student_id)

        return student, HTTPStatus.OK

    @students_namespace.expect(student_model)
    @students_namespace.marshal_with(student_model)
    @jwt_required()
    def put(self, student_id):
        """
            Update a student by id 
        """

        student_to_update=Student.get_by_id(student_id)

        data=students_namespace.payload

        student_to_update.full_name=data['full_name']
        student_to_update.email=data['email']
        
        db.session.commit()

        return student_to_update, HTTPStatus.OK

    @students_namespace.marshal_with(student_model)
    @jwt_required()
    def delete(self, student_id):
        """
            Delete a student by id
        """
        student_to_delete=Student.get_by_id(student_id)

        student_to_delete.delete()

        return student_to_delete, HTTPStatus.OK