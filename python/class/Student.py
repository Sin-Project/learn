#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' python test class '''

__author__ = 'magce';

class Student(object):
	pass;

print dir(Student);
''' ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
... '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
... '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']'''

print dir(Student.__class__);
''' ['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__',
... '__delattr__', '__dict__', '__dictoffset__', '__doc__', '__eq__', '__flags__', '__format__',
... '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__instancecheck__',
... '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__',
... '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
... '__subclasscheck__', '__subclasses__', '__subclasshook__', '__weakrefoffset__', 'mro']'''

bart = Student();

print bart;
#	<__main__.Student object at 0x10a67a590>

print Student;
#	<class '__main__.Student'>

bart.name = 'Bart Simpson';
print bart.name;
#	Bart Simpson

class Person(object):
	def run(self):
		print '%s is running...' % self.__class__.__name__;

class Student(Person):

    def __init__(self, name, score):
        self.set_name(name);
        self.set_score(score);

    def print_score(self):
    	print '%s : %s' % (self.__name, self.__score);

    def get_name(self):
    	return self.__name;

    def get_score(self):
    	return self.__score;

    def set_name(self, name):
    	if name != '' and len(name) > 2:
    		self.__name = name;
    	else:
    		raise ValueError('bad name');

    def set_score(self, score):
    	if 0 <= score <= 100:
            self.__score = score;
        else:
            raise ValueError('bad score');

bart = Student('Bart Simpson', 99);
bart.print_score();
#	Bart Simpson : 99

bart.run();

print isinstance(bart, Student);
print isinstance(bart, Person);
#	True

print type(bart);
#	<class '__main__.Student'>

import types
print type('abc')==types.StringType # types.UnicodeType types.ListType types.TypeType
# True

if hasattr(bart, 'sex'):
	getattr(bart, 'sex');
else:
	setattr(bart, 'sex', 'female');
	print 'add attr sex : %s' % bart.sex;
#	add attr sex : female

print getattr(bart, 'teacher', 404);
#	404
