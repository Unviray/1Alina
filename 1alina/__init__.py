"""
1alina
======

Entry point of project include create_app function.
"""

from flask import Flask

from .views import main


def create_app(config="1alina.settings"):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    load_views(app)
    
    return app


def load_views(app):
    app.register_blueprint(main.bp)
