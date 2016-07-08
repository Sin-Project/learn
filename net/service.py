#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, socket, threading;

def tcplink(sock, addr):
	print 'Accept new connection from %s : %s...' % addr;
	sock.send('Welcome!');
	while True:
		data = sock.recv(1024);
		time.sleep(1);
		if data == 'exit' or not data:
			break;
		sock.send('Hello, %s!' % data);
	sock.close();
	print 'Connection from %s : %s closed.' % addr;

# create connect  AF_INET : IPv4 ; SOCK_STREAM : TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

s.bind(('127.0.0.1', 9999));

# Number of connect 
s.listen(5);
print 'Waiting for connection...';

while True:
    # accept new connect:
    sock, addr = s.accept();
    # create new process for TCP:
    t = threading.Thread(target=tcplink, args=(sock, addr));
    t.start();
