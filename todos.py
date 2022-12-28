import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from app import create_app, db
# from app.models import Airport, Flight, Location
import app.models as m

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
admin = Admin(app, name='todos', template_mode='bootstrap4')
# admin.add_view(ModelView(Airport, db.session))
# admin.add_view(ModelView(Flight, db.session))
# admin.add_view(ModelView(Location, db.session))

admin.add_views(
    m.AirportView(m.Airport, db.session),
    ModelView(m.Flight, db.session),
    ModelView(m.Location, db.session)
)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Airport=m.Airport, Flight=m.Flight, Location=m.Location)