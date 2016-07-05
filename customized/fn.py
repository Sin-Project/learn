#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' customized function '''

__author__ = 'magce';

# for in  return str
def fullToStr(params):
	includes = '';
	for value in params:
		if value == params[-1]:
			includes += str(value);
		else:
			includes += str(value) + ', ';
	return includes;

def readObjectAttr(obj, attr):
    if hasattr(obj, attr):
        return obj.attr;
    return None

# try:
#     print 'try...'
#     r = 10 / int(2);
#     print 'result:', r
# except ValueError, e:
#     print 'ValueError:', e
# except ZeroDivisionError, e:
#     print 'ZeroDivisionError:', e
# else:
#     print 'no error!'
# finally:
#     print 'finally...'
# print 'END'
#
# 	try...
# 	result: 5
# 	no error!
# 	finally...
# 	END


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def domain():
    try:
        bar('0');
    except StandardError, e:
        print 'Error : %s!' % e;
    finally:
        print 'finally...'
# domain();
#	Error : integer division or modulo by zero!
#	finally...



def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
    	assert isinstance(s, int), 'type error';
    	assert s != 0, 'zero';
        return foo(s) * 2;
    except StandardError, e:
        print 'Error!'
        raise

def domain():
    bar(0);
# raise error     when (assert = false) ,active error


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def domain():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

#   domain();
#   print 'END';
# 	...
# 	ZeroDivisionError: integer division or modulo by zero
# 	END


import logging;
logging.basicConfig(level=logging.INFO);

#   s = '0';
#   n = int(s);
#   logging.info('n = %d' % n);
#   print 10 / n;
#   $ python err.py
#   INFO:root:n = 0
#   Traceback (most recent call last):
#     File "err.py", line 8, in <module>
#      print 10 / n
#   ZeroDivisionError: integer division or modulo by zero