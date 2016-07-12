#!/usr/bin/env python
# -*- coding: utf-8 -*-
# web.py
CONTENT_TYPE = 'text/html;charset=utf-8';

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')]);
    unicodeText = u'<h1>hello, %s!</h1><small> %s </small>' % (environ['PATH_INFO'][1:] or 'web', environ['LOGNAME']);
    return unicodeText.encode('utf-8');
