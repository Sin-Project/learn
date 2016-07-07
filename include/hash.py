#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib;

md5 = hashlib.md5();
md5.update('how to use md5');
print md5.hexdigest();
#	08b9239f92786f609443b669d5a041c1

md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest();
#	d26a53750bc40b38b65a520292f69306


sha1 = hashlib.sha1();
sha1.update('how to use sha1 in ');
sha1.update('python hashlib?');
print sha1.hexdigest();
#	2c76b57293ce30acef38d98f6046927161b46a44