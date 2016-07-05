#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re;

print re.match(r'^\d{3}\-\d{3,8}$', '010-12345');
#	<_sre.SRE_Match object at 0x1026e18b8>
#	match success return Match object, worng return None

test = '123456789';
if re.match(r'[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}', test):
    print 'ok';
else:
    print 'failed';
#	failed

print re.split(r'[\s\,\;]+', 'a,b;; c  d')
#	['a', 'b', 'c', 'd']

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
# 	'010-12345'
print m.group(1)
# 	'010'
print m.group(2)
# 	'12345'

t = '19:05:30';
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t);
print m.groups();
#	('19', '05', '30')

print re.match(r'^(\d+)(0*)$', '102300').groups()
#	('102300', '')
print re.match(r'^(\d+?)(0*)$', '102300').groups()
#	('1023', '00')

# precompile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$');

print re_telephone.match('010-12345').groups();
#	('010', '12345')
print re_telephone.match('010-8086').groups();
#	('010', '8086')

email = '<Tom Paris> someone@gmail.com';
print re.match(r'^(<[\w\s]*>\s*)?([0-9a-zA-Z]+)@([0-9]{1,6}|[a-z]{2,9}).([a-zA-z]{2,3})$', email).groups();
#	('<Tom Paris> ', 'someone', 'gmail', 'com')