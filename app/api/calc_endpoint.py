"""This module exposes a resource for calculating numbers."""

from flask_restful import Resource


class Sum(Resource):
    """This is the Sum class."""

    def get(self, num_1, num_2):
        """ sum two numbers """
        return num_1 + num_2


class Sub(Resource):
    """ This is the Sub class """

    def get(self, num_1, num_2):
        """ sub two numbers """
        return num_1 - num_2

class Mul(Resource):
    """ The Mul class """

    def get(self, num_1, num_2):
        """ multiply two numbers """
        return num_1 * num_2

class Div(Resource):
    """ The div class """
    def get(self, num_1, num_2):
        """ divides two numbers """
        return num_1 / num_2
        