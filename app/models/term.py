from . import db


class Term(db.Model):
    __tablename__ = 'term'
    id = db.Column(db.Integer, primary_key=True)
    courses = db.relationship('Course', backref='term')

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
