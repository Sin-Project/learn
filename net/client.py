#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

s.connect(('127.0.0.1', 9999));
# print recv:
print s.recv(1024);
for data in ['Michael', 'Tracy', 'Sarah']:
    # send data:
    s.send(data);
    print s.recv(1024);
s.send('exit');
s.close();


# UDP
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in ['Michael', 'Tracy', 'Sarah']:
#     # 发送数据:
#     s.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print s.recv(1024)
# s.close()