#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' python test class '''

__author__ = 'magce';

class Student(object):
	pass;

# print dir(Student);
# ''' ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
# ... '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# ... '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']'''

bart = Student();

print bart;
#	<__main__.Student object at 0x10a67a590>

print Student;
#	<class '__main__.Student'>

bart.name = 'Bart Simpson';
print bart.name;
#	Bart Simpson

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student('Bart Simpson', 99);
print 'Student name : %s, score : %i' % (bart.name, bart.score);
#	Student name : Bart Simpson, score : 99