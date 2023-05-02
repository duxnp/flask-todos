from .db import db

class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    airport_id = db.Column(db.Integer, db.ForeignKey('airports.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def __repr__(self) -> str:
        return self.number
