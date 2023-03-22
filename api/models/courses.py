from ..utils import db

class Course(db.Model):
    __tablename__='courses'
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(225),nullable=False,unique=True)
    teacher=db.Column(db.String(225),nullable=False,unique=True)

    def __repr__(self):
        return f'<Course {self.name}>'