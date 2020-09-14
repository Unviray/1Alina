"""
1alina
======

Entry point of project include create_app function.
"""

from flask import Flask


def create_app(config="1alina.settings"):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)
    
    return app