from flask_admin.contrib.sqla.view import ModelView, func

class AirportView(ModelView):
    can_create = False
    can_edit = False
    can_delete = False
    can_view_details = True
    column_descriptions = dict(
        name='Airport Name'
    )
    column_labels = dict(name='Name')
    column_searchable_list = ['name']
    form_excluded_columns = ['flights']
    page_size = 5

    # Example of restricting records that appear in an admin view
    # def get_query(self):
    #     return self.session.query(self.model).filter(
    #         self.model.name.like('a%')
    #     )
    # def get_count_query(self):
    #     return self.session.query(func.count('*')).filter(
    #         self.model.name.like('a%')
    #     )
