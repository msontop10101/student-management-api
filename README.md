## STUDENT MANAGEMENT API

# Introduction

1. This is a student management api containing routes for adding a student, removing a student, updating a student data, and getting all the students data.

2. The student management api contains routes for adding course, removing, updating and getting all the courses data

3. Authentication and authorization was done JWT 


## MY API ROUTES

<table>
  <tr>
    <th>Function</th>
    <th>Method</th>
    <th>Route</th>
  </tr>
  <tr>
    <td>Signing up user</td>
    <td>POST</td>
    <td>http://moyosoreelijah.pythonanywhere.com/auth/signup</td>
  </tr>
  <tr>
    <td>User Login</td>
    <td>POST</td>
    <td>http://moyosoreelijah.pythonanywhere.com/auth/login</td>
  </tr>
  <tr>
    <td>Get All Students</td>
    <td>GET</td>
    <td>http://moyosoreelijah.pythonanywhere.com/students/students</td>
  </tr>
  <tr>
    <td>Adding a new student</td>
    <td>POST</td>
    <td>http://moyosoreelijah.pythonanywhere.com/students/students</td>
  </tr>
  <tr>
    <td>Getting a single student</td>
    <td>GET</td>
    <td>http://moyosoreelijah.pythonanywhere.com/students/student/{student_id}</td>
  </tr>
  <tr>
    <td>Deleting a new student</td>
    <td>DELETE</td>
    <td>http://moyosoreelijah.pythonanywhere.com/students/student/{student_id}</td>
  </tr>
  <tr>
    <td>Updating a student data</td>
    <td>PUT</td>
    <td>http://moyosoreelijah.pythonanywhere.com/students/student/{student_id}</td>
  </tr>
  <tr>
    <td>Getting all courses</td>
    <td>GET</td>
    <td>http://moyosoreelijah.pythonanywhere.com/courses/courses</td>
  </tr>
  <tr>
    <td>Adding a course</td>
    <td>POST</td>
    <td>http://moyosoreelijah.pythonanywhere.com/courses/courses</td>
  </tr>
  <tr>
    <td>Getting a single course by ID</td>
    <td>GET</td>
    <td>http://moyosoreelijah.pythonanywhere.com/courses/course/{course_id}</td>
  </tr>
  <tr>
    <td>Deleting a single course</td>
    <td>DELETE</td>
    <td>http://moyosoreelijah.pythonanywhere.com/courses/course/{course_id}</td>
  </tr>
  <tr>
    <td>Updating a course</td>
    <td>PUT</td>
    <td>http://moyosoreelijah.pythonanywhere.com/courses/course/{course_id}</td>
  </tr>
</table>