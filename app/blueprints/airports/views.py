from flask import redirect, render_template, request, url_for, jsonify, abort, flash
from sqlalchemy.orm import joinedload, noload, contains_eager
from marshmallow import ValidationError

from app.extensions import db
from app.models import Airport
from app.schemas import AirportSchema

from . import airports

@airports.route('/airport/dump-test')
def dump_test():
    try:
        schema = AirportSchema()

        airport_json = {
            # "name": "Smart Airport Name",
            "unknownField": "This will be ignored"
        }
        airport = schema.load(airport_json)

        # airport = Airport.query.get(1)
        # airport = db.session.query(Airport)\
        #     .options(joinedload(Airport.flights))\
        #     .filter(Airport.id == 1)\
        #     .one()
        
        airports = db.session.query(Airport)\
            .options(joinedload(Airport.flights))\
            .all()

        return jsonify(schema.dump(airport)), 200
        # return jsonify(schema.dump(airports, many=True)), 200
    except ValidationError as error:
        return jsonify(error.messages)