from . import db


class Student(db.Model):
    __tablename__ = 'student'
    pidm = db.Column(db.Integer, primary_key=True)  # pidm
    name = db.Column(db.String(64), unique=True)
    internship = db.relationship('Internship', backref='student')

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
