#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools;
natuals = itertools.count(1);

# for n in natuals:
# 	print n;
# 	Output natural number ， Can't stop by self.

abc = itertools.cycle('ABC');

# for n in abc:
# 	print n;
#	Output 'A' 'B' 'C' ， Can't stop by self.

a = itertools.repeat('A', 10);
# for n in a:
# 	print n;
# 	Output ‘A’ 10 times

ns = itertools.takewhile(lambda x: x <= 10, natuals);
# for n in ns:
# 	print n;
# 	1-10

for n in itertools.chain('ABC', 'XYZ'):
	print n;
#	ABCXYZ

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print key, list(group);
# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']

for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
	print x;
# 	10
# 	40
# 	90
# imap return iterable object

r = map(lambda x: x*x, [1, 2, 3])
print r 
# return list
#	[1, 4, 9]

r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
	print n;
# 	1
# 	4
# 	9
# 	16
# 	25
# 	36
# 	49
# 	64
# 	81

# map(lambda x: x*x, itertools.count(1));  Can't handl the infinite sequence

# itertools.imap() : map() / itertools.ifilter() : ifilter()


