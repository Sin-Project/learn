#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64;

print base64.b64encode('users\\\x00string');
#	dXNlcnNcAHN0cmluZw==

print base64.b64decode('dXNlcnNcAHN0cmluZw==');
 #	users\string

print base64.b64encode('i\xb7\x1d\xfb\xef\xff');
#	'abcd++//'

print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff');
#	abcd--__

print base64.urlsafe_b64decode('abcd--__');
#	'i\xb7\x1d\xfb\xef\xff'

print base64.b64decode('YWJjZA==')
#	'abcd'
# print base64.b64decode('YWJjZA')
# 	TypeError: Incorrect padding

def safe_b64decode(ss):
    return base64.b64decode(''.join([ss,'='*(len(ss)%4)]))

print safe_b64decode('YWJjZA');
#	'abcd'
