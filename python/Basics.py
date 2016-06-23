#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' python basics '''

__author__ = 'magce';
__source__ = 'Michael Liao';

import customized.fn as fn;

# int 
integer = 1546685;
print dir(integer);
''' ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', 
...'__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', 
...'__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', 
...'__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', 
...'__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__',
... '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
... '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__',
... '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__',
... '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__',
... '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']'''

print '\n';

# string 
string = 'asbdsqwe';
print dir(string);
'''['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__',
... '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
... '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
... '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
... '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser',
... 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find',
... 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle',
... 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex',
... 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
... 'swapcase', 'title', 'translate', 'upper', 'zfill']'''


# list
classmates = ['Mechael', 'Bob', 'Tracy'];
classmates.sort();

classmates.append(123);
classmates.append('Pop1');
classmates.insert(1, True);
classmates.insert(1, 'Pop2');
classmates.pop();
classmates.pop(1);

print '''\n This list\'s length : %i, include : %s 
 The last element : %s \n''' % (len(classmates), fn.fullToStr(classmates), classmates[-1]);
#	This list's length : 5, include : Mechael, True, Bob, Tracy, 123 
#	The last element : 123 


# tuple
assemble = ('a', 'b', ['A', 'B']);
assemble[2][0] = 'X';
print assemble;
#	('a', 'b', ['X', 'B'])
for x in assemble:
	#if isinstance(x, iterable): # python 2.7.11 Error
	#	for xx in x:
	#		print xx;
	#else:
		print x;
#	a 	b 	['X', 'B']


# dict dictionary
score = [100, 90 , 0, 60, 50];
myClass = {}; 
i = 0;
for value in classmates:
	myClass[str(value)] = score[i];
	i += 1;
myClass['Mechael'] = 66;

print 'SS' in myClass;
#	False
print myClass.get('SS');
#	None
print myClass.get('SS', 'null');
#	null

myClass['SS'] = 55;
myClass.pop('SS');
print myClass;
# 	{'Mechael': 66, 'Bob': 0, '123': 50, 'True': 90, 'Tracy': 60}


# set  Not repeat collection
mySet1 = set([1, 1, 2, 2, 3]);
mySet2 = set([1, 2, 4, 3]);
mySet1.add(4);
mySet1.remove(4);
print mySet1;
#	set([1, 2, 3])
print mySet1 & mySet2;
#	set([1, 2, 3])
print mySet1 | mySet2;
#	set([1, 2, 3, 4])