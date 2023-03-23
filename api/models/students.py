from ..utils import db

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer(),primary_key=True)
    full_name=db.Column(db.String(225),nullable=False,)
    email=db.Column(db.String(225),nullable=False,unique=True)

    def __repr__(self):
        return f'<Student {self.full_name}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()