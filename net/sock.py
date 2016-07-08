#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket;

# create connect   AF_INET : IPv4 ; SOCK_STREAM : TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

s.connect(('www.sina.com.cn', 80));

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n');

buffer = [];
while True:
    # limit 1kb:
    d = s.recv(1024);
    if d:
        buffer.append(d);
    else:
        break;
data = ''.join(buffer);

s.close();

header, html = data.split('\r\n\r\n', 1);
print header;
# write file:
with open('/Users/magce/Documents/sina.html', 'wb') as f:
    f.write(html);

# HTTP/1.1 200 OK
# Date: Fri, 08 Jul 2016 03:16:41 GMT
# Server: PWS/8.1.38
# X-Px: ht h0-s1021.p12-sjc.cdngp.net
# Cache-Control: max-age=120
# Expires: Fri, 08 Jul 2016 03:17:17 GMT
# Age: 84
# Accept-Ranges: bytes
# Content-Length: 604933
# Content-Type: text/html
# Last-Modified: Fri, 08 Jul 2016 03:13:05 GMT
# Connection: close