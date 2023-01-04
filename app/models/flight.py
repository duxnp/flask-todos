from flask_admin.contrib.sqla.view import ModelView, func

from . import db


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
