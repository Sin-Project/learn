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

