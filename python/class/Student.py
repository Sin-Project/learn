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

class Adult(object):
    def work(self):
        print '%s is working...' % self.__class__.__name__;

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
        if not isinstance(name, str):
            raise ValueError('score must be an string!');
    	if name != None and len(name) > 2:
    		self.__name = name;
    	else:
    		raise ValueError('bad name');

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
    	if 0 <= score <= 100:
            self.__score = score;
        else:
            raise ValueError('bad score');

    def __str__(self):
        return 'Student object (name: %s)' % self.__name;

    __repr__ = __str__;

bart = Student('Bart Simpson', 99);
bart.print_score();
#	Bart Simpson : 99

bart.run();
#   Student is running...

print bart;
#   Student object (name: Bart Simpson)


print isinstance(bart, Student);
print isinstance(bart, Person);
#	True

print type(bart);
#	<class '__main__.Student'>

import types
print type('abc')==types.StringType # types.UnicodeType types.ListType types.TypeType
# True

if hasattr(bart, 'sex'):
	print getattr(bart, 'sex');
else:
	setattr(bart, 'sex', 'female');
	print 'add attr sex : %s' % bart.sex;
#	add attr sex : female

print getattr(bart, 'teacher', 404);
#	404

#   function bind
def set_age(self, age):
    self.__age = age;
def get_age(self):
    return self.__age;

from types import MethodType;
bart.set_age = MethodType(set_age, bart, Student);
bart.get_age = MethodType(get_age, bart, Student);
#   bind function in instance
bart.set_age(55);
print bart.get_age;
#   <bound method Student.get_age of <__main__.Student object at 0x1019f1b10>>
print bart.get_age();
#   55

sam = Student('Sam Tomas', 60);
#   sam.set_age(52);
#   AttributeError: 'Student' object has no attribute 'set_age'

Student.set_age = MethodType(set_age, None, Student);
#   bind function in class

#   limit class attr : __slots__
class GraduateStudent(object):
    __slots__ = ('name', 'age');

mike = GraduateStudent();
mike.name = 'little mike';
# mike.birth = '1983-10-30';
#   AttributeError: 'GraduateStudent' object has no attribute 'birth'

class Teacher(Person, Adult):
    """docstring for Teacher Class"""

    def __init__(self, birth):
        super(Teacher, self).__init__();
        self._birth = birth;

    @property
    def birth(self):
        return self._birth;

    @property
    def name(self):
        return self._name;

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('name must be an string!');
        if name != None and len(name) > 2:
            self._name = name;
        else:
            raise ValueError('bad name');
    @property
    def age(self):
        return self._age;

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('age must be an integer!')
        if 0 <= age <= 100:
            self._age = age;
        else:
            raise ValueError('wrong');

morel = Teacher('2016-4-6');
morel.name = 'morel skel'; #    bind property name call function name.setter
print morel.name; #     call function name  
#   morel.birth = 'ssss';
#   AttributeError: can't set attribute
print morel.birth;
#   2016-4-6
morel.run();
morel.work();