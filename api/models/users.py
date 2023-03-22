from ..utils import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(225),nullable=False,)
    email=db.Column(db.String(225),nullable=False,unique=True)
    password_hash=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()