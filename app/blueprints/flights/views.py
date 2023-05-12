from flask import redirect, render_template, request, url_for, jsonify, abort, flash
from sqlalchemy.orm import joinedload, noload, contains_eager
from marshmallow import ValidationError

from app.extensions import db
from app.models import *
from app.schemas import FlightSchema

from . import flights

# Reusable query builder
flights_statement = db.select(Flight)\
    .outerjoin(Airport)\
    .outerjoin(Location)\
    .options(
        contains_eager(Flight.airport),
        contains_eager(Flight.destination)
    )
airports_statement = db.select(Airport)
locations_statement = db.select(Location)

@flights.route("/flights", methods=['GET'])
def index():
    """Display list of flights."""
    # flights = Flight.query.get_or_404(1)
    # flights = db.session.execute(db.select(Flight).filter_by(id=1)).one()
    # flights = db.session.execute(db.select(Flight).filter_by(id=1)).scalars().all()
    # flights = db.session.execute(db.select(Flight)).scalars().all()
    # flights = db.session.execute(db.select(Flight))
    # flights_foo = db.get_or_404(Flight, 1)
    flights = db.session.scalars(flights_statement)
    return render_template('flights/index.html', flights=flights)

@flights.route("/flight/load-test")
def load_test():
    try:
        flight_schema = FlightSchema()

        # If you were creating a new flight and airport at the same time
        # Of course you wouldn't have any IDs yet
        # You can probably have one schema but have a different load configuration
        # depending on the endpoint
        # new_flight_json = {
        #     "id": "-1",
        #     "number": "666",
        #     "airport_id": "-1",
        #     "airport": {
        #         "id": "-1",
        #         "name": "My Fake Airport",
        #     },
        # }
        # new_flight = flight_schema.load(new_flight_json, partial=True)

        update_flight_json = {
            # "number": "666",
            "airport": {
                "name": "My Fake Airport",
            },
            "destination_id": "1"
        }

        new_flight = flight_schema.load(update_flight_json, partial=("airport_id",))

        # db.session.add(flight)
        # db.session.flush()
        # db.session.commit()
        # flight = Flight.query.first()
        
        # print(f"AIRPORT ID: {new_flight.airport_id}")
        return jsonify(flight_schema.dump(new_flight))
    except ValidationError as error:
        return jsonify(error.messages)

@flights.route("/flight/update-test", methods=['GET'])
def update_test():
    # Maybe a partial update only works if load_instance=True
    flight_schema = FlightSchema(load_instance=True)

    # existing_flight = Flight.query.get(1)

    existing_flight_json = {
        "id": "1",
        # "number": "1",
        # "airport_id": 3,
        # "destination_id": 2
    }
    existing_flight = flight_schema.load(existing_flight_json, partial=True)

    update_flight_json = {
        "number": "9000",
    }

    # new_flight = FlightSchema(partial=True).load(update_flight_json)
    data = flight_schema.load(update_flight_json, instance=existing_flight, partial=True)

    # db.session.add(flight)
    # db.session.flush()
    db.session.commit()
    # flight = Flight.query.first()

    return jsonify(FlightSchema().dump(data))

@flights.route("/flight/dump-test", methods=['GET'])
def dump_test():
    flight_schema = FlightSchema()
    # flight = Flight.query.first()
    # flight = Flight.query.options(joinedload(Airport.flights)).first()
    # flight = Flight.query.options(noload('airport')).first()
    # flight = Flight.query.join(Airport).first()


    flight = db.session.query(Flight)\
        .options(joinedload(Flight.airport))\
        .filter(Flight.id == 1)\
        .one()

    airport_loaded = False
    load_triggered = False

    # if flight.airport:
    #     load_triggered = True 

    # if 'airport' in flight.__dict__:
    #     airport_loaded = True

    # response = {
    #     "id": flight.id,
    #     "number": flight.number,
    #     "airport_loaded": airport_loaded,
    # }
    # return jsonify(response), 201

    return jsonify(flight_schema.dump(flight))

@flights.route("/flights/create", methods=['GET'])
def create():
    """Display form to create a new flight."""
    airports = db.session.scalars(airports_statement)
    locations = db.session.scalars(locations_statement)
    return render_template('flights/create.html', airports=airports, locations=locations)

@flights.route("/flights/save", methods=['POST'])
def save():
    """Persist the new flight."""
    # errors = create_flight_schema.validate(request.form)
    # if errors:
    #     abort(400, str(errors))

    try:
        # flight_schema = CreateFlightInputSchema()
        flight_schema = FlightSchema()
        flight = flight_schema.load(request.form)

        # flight = Flight()
        # flight.number = request.form['number']
        # flight.airport_id = request.form['airport_id']
        # flight.destination_id = request.form['destination_id']

        db.session.add(flight)
        db.session.commit()

        return redirect(url_for('flights.index'))
    except ValidationError as error:
        flash(error.messages)
        return redirect(url_for('flights.create'))


@flights.route("/flights/edit/<id>", methods=['GET'])
def edit(id):
    """Display form to edit an existing flight."""
    flight_statement = flights_statement.filter(Flight.id == id)
    flight = db.one_or_404(flight_statement)

    # flight_statement = db.select(Flight).filter_by(id=id)
    # flight = Flight.query.get_or_404(id)
    # flight = db.session.scalars(statement).one()
    # flight = db.session.scalar(flight_statement)

    airports = db.session.scalars(airports_statement)
    locations = db.session.scalars(locations_statement)

    return render_template('flights/edit.html', flight=flight, airports=airports, locations=locations)

@flights.route("/flights/update/<id>", methods=['POST'])
def update(id):
    """Persist the flight changes."""
    try:
        flight_schema = FlightSchema(load_instance=True)

        flight_statement = db.select(Flight).filter_by(id=id)
        existing_flight = db.session.scalar(flight_statement)

        # errors = flight_schema.validate(request.form)
        # if errors:
        #     abort(400, str(errors))

        flight = flight_schema.load(request.form, instance=existing_flight, partial=True)

        # flight.number = request.form['number']
        db.session.commit()

        return redirect(url_for('flights.edit', id=id))
    except ValidationError as error:
        
        flash(error.messages)
        return redirect(url_for('flights.edit', id=id))

@flights.route("/flights/delete/<id>")
def delete(id):
    """Delete the flight."""
    flight_statement = db.select(Flight).filter_by(id=id)
    flight = db.session.scalar(flight_statement)
    db.session.delete(flight)
    db.session.commit()
    return redirect(url_for('flights.index'))