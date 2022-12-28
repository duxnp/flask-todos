from . import db

class Airport(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    flights = db.relationship('Flight', backref='airport')

    def __repr__(self) -> str:
        return '<Airport %r>' % self.name

class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    airport_id = db.Column(db.Integer, db.ForeignKey('airports.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def __repr__(self) -> str:
        return '<Flight %r>' % self.number

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    flights = db.relationship('Flight', backref='destination')

    def __repr__(self) -> str:
        return '<Location %r>' % self.id