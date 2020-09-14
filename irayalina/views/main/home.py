"""
irayalina.views.main.home
=========================

Home page.
"""

from irayalina.utils import templated


@templated("home.html")
def entry():
    return {}