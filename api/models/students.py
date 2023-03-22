from ..utils import db

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer(),primary_key=True)
    full_name=db.Column(db.String(225),nullable=False,)
    email=db.Column(db.String(225),nullable=False,unique=True)

    def __repr__(self):
        return f'<Student {self.full_name}>'