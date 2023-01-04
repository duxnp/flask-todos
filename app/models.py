from . import db
from flask_admin.contrib.sqla.view import ModelView, func


class Airport(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    flights = db.relationship('Flight', backref='airport')

    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name


class AirportView(ModelView):
    column_descriptions = dict(
        name='Airport Name'
    )
    column_labels = dict(name='Name')
    column_searchable_list = ['name']
    form_excluded_columns = ['flights']
    page_size = 5

    def get_query(self):
        return self.session.query(self.model).filter(
            self.model.name.like('a%')
        )

    def get_count_query(self):
        return self.session.query(func.count('*')).filter(
            self.model.name.like('a%')
        )


class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    airport_id = db.Column(db.Integer, db.ForeignKey('airports.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def __repr__(self) -> str:
        return self.number


class FlightView(ModelView):
    # column_choices = {
    #     'airport': [('id', 'name')]
    # }
    can_view_details = True
    column_formatters = dict(
        airport=lambda v, c, m, p: m.airport.name,
        destination=lambda v, c, m, p: f'{m.destination.city}, {m.destination.country}'
    )
    # form_ajax_refs = {
    #     'user': QueryAjaxModelLoader('user', db.session, User, fields=['email'], page_size=10)
    # }
    form_ajax_refs = {
        'airport': {
            'fields': ('name',),
            'placeholder': 'Please select',
            'page_size': 10,
            'minimum_input_length': 0,
        }
    }

    def get_query(self):
        return self.session.query(self.model).filter(
            self.model.destination.has(city='Cherry Hill')
        )

    def get_count_query(self):
        return self.session.query(func.count('*')).filter(
            self.model.destination.has(city='Cherry Hill')
        )


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
    column_filters = ['country']
    inline_models = (Flight,)
