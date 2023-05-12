from flask import Blueprint

flights = Blueprint('flights', __name__)

from . import views