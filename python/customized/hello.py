#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' test module '''

import sys;

try:
    import cStringIO as StringIO;
except ImportError: # get ImportError
    import StringIO;

try:
    import json; # python >= 2.6
except ImportError:
    import simplejson as json; # python <= 2.5

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!';
    elif len(args) == 2:
        print 'Hello, %s!' % args[1];
    else:
        print 'Too many arguments!';

if __name__ == '__main__':
    test();