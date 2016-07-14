#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('test.db');
# Cursor
cursor = conn.cursor();
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))');
# <sqlite3.Cursor object at 0x10f8aa260>
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')');
# <sqlite3.Cursor object at 0x10f8aa260>
# rowcount : get insert row count
cursor.rowcount;
# 1
# close Cursor
cursor.close();
# commit Event
conn.commit();
conn.close();

# mysql
import mysql.connector;
conn = mysql.connector.connect(user='root', password='123456', database='test', use_unicode=True);
cursor = conn.cursor();
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))');
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael']);
cursor.rowcount;
conn.commit();
cursor.close();
cursor = conn.cursor();
cursor.execute('select * from user where id = %s', ('1',));
values = cursor.fetchall();
print values;
#	[(u'1', u'Michael')]
cursor.close();
conn.close();

# SQLAlchemy To be continued