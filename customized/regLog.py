#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time;
import hashlib;

time_salt = str(time.time());

def pas2md5(usename, password):
	md5 = hashlib.md5();
	salt = usename + time_salt;
	md5.update(password + salt);
	return md5.hexdigest();

def pas2sha1(usename, password):
    sha = hashlib.sha1();
    salt = usename + time_salt;
    sha.update(password + salt);
    return sha.hexdigest();

db_client = {};

while 1:
    op = raw_input('Please select you need :\n 1 : register\n 2 : login\n 3 : exit\n ');
    if op == '1':
        print 'register...\n'
        name = raw_input('input your name : ')
        keywords =  raw_input('input your password : ')
        cho = raw_input('select Encryption mode :\n 1 : md5\n 2 : sha1\n ');
        if cho == '1':
            password = pas2md5(name.lower(), keywords);
            print 'MD5-Success...\n';
        else:
            password = pas2sha1(name.lower(), keywords);
            print 'SHA1-Success...\n';

        db_client[name.lower()] = password;
        print db_client;

    elif op == '2':
        print 'login...\n';
        name_req = raw_input('input username :');
        keywords_req = raw_input('input password :');

        if name_req in db_client:
        	if db_client[name_req.lower()] == pas2md5(name_req, keywords_req) or db_client[name_req.lower()] == pas2sha1(name_req, keywords_req):
	        	print '\n====================================\n';
	        	print 'welcome %s' % name_req;
	        	print '\n====================================\n';
	        else:
	        	print '\npassword error\n';
        else:
            print '\nUser does not exist\n';

    elif op == '3':
        print 'exit...';
        break;

    else:
    	print 'enter error, please reinput!\n';