from . import db


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    street_address = db.Column(db.String(64), unique=True)
    city = db.Column(db.String(64), unique=True)

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
