
from .db import db

class Airport(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    flights = db.relationship('Flight', backref='airport')

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name

