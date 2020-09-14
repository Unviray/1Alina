"""
irayalina.views.main
=================

Main views.
"""

from flask import Blueprint

from . import home


bp = Blueprint("main", __name__)


bp.add_url_rule(
    rule="/",
    endpoint="home",
    view_func=home.entry, )