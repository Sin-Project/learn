#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr(n & 0xff)
s = b1 + b2 + b3 + b4
print s;
#	'\x00\x9c@c';

import struct;
print struct.pack('>I', 10240099); # > : big-endian  , I 4bit nosign int.
#	'\x00\x9c@c'

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80'); # H 2bit nosign int.
#	(4042322160, 32896);
