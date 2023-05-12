from marshmallow import fields, validates_schema, validates, ValidationError, EXCLUDE, post_load
from marshmallow.validate import Length, Range
from marshmallow_sqlalchemy.fields import Nested

from app.extensions import ma, SmartNested, BaseSchema
from app.models import Flight


class FlightSchema(BaseSchema):
    """Flight model serialization, deserialization, and validation."""
    class Meta(BaseSchema.Meta):
        model = Flight
        # load_instance = True
        unknown = EXCLUDE

    id = ma.auto_field()
    number = ma.auto_field(required=True, validate=Length(min=1), 
        error_messages={"required": "Please provide a flight number."})
    airport_id = ma.auto_field(required=True)
    destination_id = ma.auto_field(required=True)

    # Providing class name as a string to avoid circular import.
    # Using exclude to avoid infinite recursion.
    airport = SmartNested('AirportSchema', exclude=("flights",))

    @validates('airport_id')
    def is_not_foo(self, data, **kwargs):
        """Making sure there aren't any dumb airport names. JUST A TEST."""
        if data == 2:
            raise ValidationError("This is a dumb airport!")
        
    @validates_schema
    def validate_test(self, data, **kwargs):
        """Receives the whole schema dictionary"""
        if len(data.get('number', '')) > 6:
            raise ValidationError('That flight number is way too long, dude!', 'number')
    
    # I commented this out to fix the problems I had when trying to have the .load() method update an existing instance
    # I think this was needed for the SmartNested() class, otherwise SmartNested() was not receiving an instance of a domain class
    # @post_load
    # def make_flight(self, data, **kwargs):
    #     return Flight(**data)