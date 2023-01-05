from . import db


class Internship(db.Model):
    __tablename__ = 'internship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.pidm'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    description = db.Column(db.String(64), unique=True)

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
