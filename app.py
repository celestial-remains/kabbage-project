
# -*- coding: utf-8 -*-
"""WSGI Application and Routes"""

import os
import sys
import webapp2
import handlers

app = webapp2.WSGIApplication(debug=True)

secure_scheme = 'https'

_routes = [
    webapp2.Route('/', handlers.IndexHandler, methods=['GET','POST']),
]

def add_routes(app, routes=_routes):
    if app.debug:
        secure_scheme = 'http'
    for r in routes:
        app.router.add(r)

add_routes(app,_routes)
