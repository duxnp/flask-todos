from flask_admin.contrib.sqla.view import ModelView, func

class FlightView(ModelView):
    can_view_details = True
    # column_choices = {
    #     'airport': [('id', 'name')]
    # }
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

    # Example of restricting records that appear in an admin view
    # def get_query(self):
    #     return self.session.query(self.model).filter(
    #         self.model.destination.has(city='Cherry Hill')
    #     )
    # def get_count_query(self):
    #     return self.session.query(func.count('*')).filter(
    #         self.model.destination.has(city='Cherry Hill')
    #     )
