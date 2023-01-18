from flask_admin.contrib.sqla.view import ModelView, func
from . import db


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

    # Example of restricting records that appear in an admin view
    # def get_query(self):
    #     return self.session.query(self.model).filter(
    #         self.model.name.like('a%')
    #     )
    # def get_count_query(self):
    #     return self.session.query(func.count('*')).filter(
    #         self.model.name.like('a%')
    #     )
