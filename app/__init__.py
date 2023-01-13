from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap4
from config import config
from app.models import db
from app.models.airport import Airport, AirportView
from app.models.flight import Flight, FlightView
from app.models.location import Location, LocationView

bootstrap = Bootstrap4()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    admin = Admin(app, name='todos',
                  base_template='layout-admin.html', template_mode='bootstrap4')
    # admin = Admin(app, name='todos', template_mode='bootstrap4')
    admin.add_views(
        AirportView(Airport, db.session),
        FlightView(Flight, db.session),
        LocationView(Location, db.session)
    )

    return app
