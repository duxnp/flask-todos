import os
from flask_migrate import Migrate
from app import create_app
from app.extensions import db
from app.models import Airport, Flight, Location

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Airport=Airport, Flight=Flight, Location=Location)
