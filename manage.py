""" main module where the things happen """
#! /usr/bin/env python

import os

from flask_script import Manager
from flask_restful import Api
from app.api import calc_endpoint

from app import create_app


APP = create_app(os.getenv('APP_CONFIG', 'default'))
MANAGER = Manager(APP)
API = Api(APP)

@MANAGER.shell
def make_shell_context():
    """ a method """
    return dict(app=APP)

API.add_resource(calc_endpoint.Sum, '/sum/<int:num_1>/<int:num_2>')
API.add_resource(calc_endpoint.Sub, '/sub/<int:num_1>/<int:num_2>')
API.add_resource(calc_endpoint.Mul, '/mul/<int:num_1>/<int:num_2>')
API.add_resource(calc_endpoint.Div, '/div/<int:num_1>/<int:num_2>')

if __name__ == '__main__':
    MANAGER.run()
