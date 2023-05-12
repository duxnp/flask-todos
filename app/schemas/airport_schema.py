from marshmallow import fields, validates_schema, validates, ValidationError, EXCLUDE, post_load

from app.extensions import ma, SmartNested, BaseSchema
from app.models import Airport

class AirportSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Airport
        unknown = EXCLUDE

    id = ma.auto_field()
    name = ma.auto_field(required=True)

    flights = ma.List(SmartNested('FlightSchema', exclude=("airport",)))

    @validates('name')
    def is_not_foo(self, data, **kwargs):
        """Making sure there aren't any dumb airport names. JUST A TEST."""
        if data == 'Dumb Airport Name':
            raise ValidationError("This is a dumb airport!")
        
    @post_load
    def make_airport(self, data, **kwargs):
        return Airport(**data)