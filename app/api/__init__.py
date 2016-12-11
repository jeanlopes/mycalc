""" This module initiates the endpoints """
from flask import Blueprint
# Import any endpoints here to make them available
from . import calc_endpoint

CALC = Blueprint('calc', __name__)