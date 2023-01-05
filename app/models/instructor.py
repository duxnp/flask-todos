from . import db


class Instructor(db.Model):
    __tablename__ = 'instructor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    courses = db.relationship('Course', backref='instructor')

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
