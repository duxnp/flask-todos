from .ma import ma
from .flight import Flight
from .smartnested import SmartNested
from .airportschema import AirportSchema

class FlightSchema(ma.SQLAlchemySchema):
    id = ma.auto_field()
    number = ma.auto_field()
    airport = SmartNested(AirportSchema)

    class Meta:
        model = Flight
        # include_fk = True
        # include_relationships = True