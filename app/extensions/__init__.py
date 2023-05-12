from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_marshmallow import Marshmallow
ma = Marshmallow()

class SmartNested(ma.Nested):
    def serialize(self, attr, obj, accessor=None):
        if hasattr(obj, '__dict__') and attr not in obj.__dict__:
            object_id = getattr(obj, attr + "_id")
            return {"id": int(object_id) if object_id else object_id}
        return super(SmartNested, self).serialize(attr, obj, accessor)
    
class BaseSchema(ma.SQLAlchemySchema):
    """
    Normally, when creating a flask_marshmallow schema class
    you would subclass SQLAlchemySchema like so::

        from flask_marshmallow import Marshmallow
        ma = Marshmallow()

        class MySchema(ma.SQLAlchemySchema):
    
    This BaseSchema solves a problem in which a reference to
    the database session is missing from the instance.
    
    Missing session workaround:
    https://github.com/marshmallow-code/flask-marshmallow/issues/44#issuecomment-1002740778
    """
    class Meta(ma.SQLAlchemySchema.Meta):
        sqla_session = db.session

