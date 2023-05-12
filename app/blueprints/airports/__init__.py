from flask import Blueprint

airports = Blueprint('airports', __name__)

from . import views