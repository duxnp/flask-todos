import os
from flask_migrate import Migrate
from app import create_app
from app.models import db
from app.models.airport import Airport
from app.models.flight import Flight
from app.models.location import Location

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Airport=Airport, Flight=Flight, Location=Location)
