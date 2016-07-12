#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server;
# import from web.py
from web import application;

# makse server，IP = ''，port 8000，handle application
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# listener
httpd.serve_forever()