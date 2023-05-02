from flask import redirect, render_template, request, url_for, jsonify
from sqlalchemy.orm import joinedload, noload

from ..models import *

from . import flights

@flights.route("/flights")
def index():
    # flights = Flight.query.get_or_404(1)

    # flights = db.session.execute(db.select(Flight).filter_by(id=1)).one()
    # flights = db.session.execute(db.select(Flight).filter_by(id=1)).scalars().all()
    # flights = db.session.execute(db.select(Flight)).scalars().all()
    flights = db.session.scalars(db.select(Flight))
    
    # flights = db.session.execute(db.select(Flight))
    # flights_foo = db.get_or_404(Flight, 1)

    return render_template('flights/index.html', flights=flights)

@flights.route("/flights-test")
def flights_test():
    flight_schema = FlightSchema()
    flight = Flight.query.first()
    # flight = Flight.query.options(joinedload(Airport.flights)).first()
    # flight = Flight.query.options(noload('airport')).first()
    # flight = Flight.query.join(Airport).first()

    # flight = db.session.query(Flight).options(joinedload(Flight.airport)).first()

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

@flights.route("/flights/edit/<id>", methods=['GET'])
def edit(id):
    airports_statement = db.select(Airport)
    locations_statement = db.select(Location)
    flight_statement = db.select(Flight).filter_by(id=1)

    airports = db.session.scalars(airports_statement)
    locations = db.session.scalars(locations_statement)
    # flight = Flight.query.get_or_404(id)
    # flight = db.session.scalars(statement).one()
    flight = db.session.scalar(flight_statement)

    return render_template('flights/edit.html', flight=flight, airports=airports, locations=locations)

@flights.route("/flights/update/<id>", methods=['POST'])
def update(id):
    form = request.form
    print(form['number'])

    flight_statement = db.select(Flight).filter_by(id=1)
    flight = db.session.scalar(flight_statement)
    flight.number = form['number']
    db.session.commit()

    return redirect(url_for('flights.edit', id=id))

