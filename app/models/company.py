from . import db


class Company(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    addresses = db.relationship('Address', backref='company')
    default_address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
