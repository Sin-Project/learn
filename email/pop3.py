#!/usr/bin/env python
# -*- coding: utf-8 -*-

import poplib;
from email.parser import Parser;

email = raw_input('Email: ');
password = raw_input('Password: ');
pop3_server = raw_input('POP3 server: ');

# connect pop3:
server = poplib.POP3(pop3_server);
server.set_debuglevel(1);
# print welcome message
print(server.getwelcome());
# login:
server.user(email);
server.pass_(password);
# stat()return Mail volume & space usage:
print('Messages: %s. Size: %s' % server.stat());
# list()return mail ID
resp, mails, octets = server.list();
# return mail list['1 82923', '2 2184', ...]
print(mails);
# fetch last mail, index from 1:
index = len(mails);
resp, lines, octets = server.retr(index);
# lines Original text message,
msg_content = '\r\n'.join(lines);
msg = Parser().parsestr(msg_content);
# print msg;
# delete mail : server.dele(index)
# close connect
server.quit();
