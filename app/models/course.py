from . import db


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    college = db.Column(db.String(64), unique=True)

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
