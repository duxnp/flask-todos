from flask_admin.contrib.sqla.view import ModelView, func
from .db import db
from .flight import Flight


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    flights = db.relationship('Flight', backref='destination')

    def __repr__(self) -> str:
        return f'{self.city}, {self.country}'


class LocationView(ModelView):
    form_excluded_columns = ['flights']
    column_filters = ['city', 'country']
    inline_models = (Flight,)
