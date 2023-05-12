import importlib
from flask_admin.contrib.sqla.view import ModelView, func
# from .utils import db
from app.extensions import db

class Airport(db.Model):
    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    flights = db.relationship('Flight', back_populates='airport')

    # Flight = importlib.import_module("app.models.flight").Flight
    
    def __repr__(self) -> str:
        # return '<Airport %r>' % self.name
        return self.name
    
    def foo(self):
        # Idea from this article
        # https://levelup.gitconnected.com/escaping-the-python-import-maze-tips-for-avoiding-circular-imports-in-python-9046b0be5cb
        # flight = self.Flight.query.get(1)
        from app.models import Flight
        flight = Flight.query.get(2)

        return f"This is actually from an instance of {self.name}. {flight.bar()}"
    
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
