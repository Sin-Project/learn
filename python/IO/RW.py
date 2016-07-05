 #!/usr/bin/env python
# -*- coding: utf-8 -*-

# read & write 

f = open('./test.txt', 'r')
#	IOError: [Errno 2] No such file or directory: './test.txt'

try:
	f = open('../Basics.py', 'r');
	print f.read();
finally:
	if f:
		f.close();

# | |
# | |
#  V

with open('/path/to/file', 'r') as f:
    print f.read(size);
#	readline() oneline,  readlines() allline return list, 
# emp:
for line in f.readlines():
    print(line.strip());

f = open('./test.jpg', 'rb');
f.read();
#	'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # x16


f = open('./gbk.txt', 'rb')
u = f.read().decode('gbk');
print u ;
#	测试(u'\u6d4b\u8bd5')

import codecs;
with codecs.open('./gbk.txt', 'r', 'gbk') as f:
    f.read(); # u'\u6d4b\u8bd5'


f = open('./test.txt', 'w');
f.write('Hello, world!');
f.close();

# | |
# | |
#  V

with open('./test.txt', 'w') as f:
    f.write('Hello, world!');