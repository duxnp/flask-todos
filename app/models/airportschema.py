from .ma import ma
from .airport import Airport

class AirportSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Airport

    id = ma.auto_field()
    name = ma.auto_field()
    # flight = ma.auto_field()