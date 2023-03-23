from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from ..models.courses import Course
from http import HTTPStatus
from ..utils import db

courses_namespace = Namespace('courses',description='Students Namespace')
courses_model = courses_namespace.model(
    'Courses', {
        'id':fields.Integer(description='An id'),
        'name':fields.String(description='Course Name'),
        'teacher':fields.String(description='The teachers name')
    }
)

@courses_namespace.route('/courses')
class CoursesGetCreate(Resource):

    @courses_namespace.marshal_with(courses_model)
    @jwt_required()
    def get(self):
        """
        Get all courses
        """

        courses=Course.query.all()

        return courses, HTTPStatus.OK

    @courses_namespace.expect(courses_model)
    @courses_namespace.marshal_with(courses_model)
    @jwt_required()
    def post(self):
        """
        Create new course
        """

        data=courses_namespace.payload

        new_course=Course(
            name=data['name'],
            teacher=data['teacher']
        )

        new_course.save()

        return new_course, HTTPStatus.CREATED
        

@courses_namespace.route('/course/<int:course_id>')
class GetUpdateDelete(Resource):
    
    @courses_namespace.marshal_with(courses_model)
    @jwt_required()
    def get(self, course_id):
        """
            Get a course by id
        """
        course=Course.get_by_id(course_id)

        return course, HTTPStatus.OK

    @courses_namespace.expect(courses_model)
    @courses_namespace.marshal_with(courses_model)
    @jwt_required()
    def put(self, course_id):
        """
            Update a course by id 
        """

        course_to_update=Course.get_by_id(course_id)

        data=courses_namespace.payload

        course_to_update.name=data['name']
        course_to_update.teacher=data['teacher']
        
        db.session.commit()

        return course_to_update, HTTPStatus.OK

    @courses_namespace.marshal_with(courses_model)
    @jwt_required()
    def delete(self, course_id):
        """
            Delete a course by id
        """
        course_to_delete=Course.get_by_id(course_id)

        course_to_delete.delete()

        return course_to_delete, HTTPStatus.OK
