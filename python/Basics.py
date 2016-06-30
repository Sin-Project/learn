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
... '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__',
... '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__',
... '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__',
... '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__',
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

from collections import Iterable;
# tuple
assemble = ('a', 'b', ['A', 'B']);
assemble[2][0] = 'X';
print assemble;
#	('a', 'b', ['X', 'B'])
for x in assemble:
	if isinstance(x, Iterable): 
		for xx in x:
			print xx;
	else:
		print x;
#	a 	b 	X 	B


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

# def function
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle);
    ny = y - step * math.sin(angle);
    return nx, ny;

r = move(100, 100, 60, math.pi / 6);
print r;
#	(151.96152422706632, 70.0)

def calc(*numbers):
    sum = 0;
    for n in numbers:
        sum = sum + n * n;
    return sum;

print calc(1, 2);
#	5
print calc();
#	0
nums = [1, 2, 100];
print calc(*nums);
#	10005

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw;


print func(1, 2);
#	a = 1 b = 2 c = 0 args = () kw = {}
print func(1, 2, c=3);
#	a = 1 b = 2 c = 3 args = () kw = {}
print func(1, 2, 3, 'a', 'b');
#	a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
print func(1, 2, 3, 'a', 'b', x=99);
#	a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
args = (1, 2, 3, 4);
kw = {'x': 99};
print func(*args, **kw);
#	a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}

def fact(n):
    if n==1:
        return 1;
    return n * fact(n - 1);
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120



def fact(n):
    return fact_iter(n, 1);

def fact_iter(num, product):
    if num == 1:
        return product;
    return fact_iter(num - 1, num * product);

print fact(5);
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120

# Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'];
#   L[:3] = L[0:3]
print L[:3];
#   ['Michael', 'Sarah', 'Tracy']
print L[-2:];
#   ['Bob', 'Jack']
print L[-2:-1];
#   ['Bob']

L = range(100);
print L[:10:2];
#   [0, 2, 4, 6, 8]
print L[::5];
#   [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

from collections import Iterable;
print isinstance('abc', Iterable);
#   True
print isinstance(123, Iterable);
#   False

print [x * x for x in range(1, 11)];
#   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print [m + n for m in 'ABC' for n in 'XYZ']
#   ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os;
print [d for d in os.listdir('.')]; # os.listdir (show the file & dir)
#   ['Basics.py', 'customized']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()];

# function
def fib(max):
    n, a, b = 0, 0, 1;
    while n < max:
        print b;
        a, b = b, a + b;
        n = n + 1;
#	fib(6) 1 1 2 3 5 8;

# generator
def fib(max):
    n, a, b = 0, 0, 1;
    while n < max:
        yield b;
        a, b = b, a + b;
        n = n + 1;
#	fib(6) <generator object fib at 0xxxxxxxx>   x = fib(6); x.next();

# map/reduce
def f(x):
   return x * x;
print map(f, range(1, 10))
#	[1, 4, 9, 16, 25, 36, 49, 64, 81]
def add(x, y):
	return x + y;
print reduce(add, range(1,101));
#	5050

# format : ['adam', 'LISA', 'barT']
frma = ['adam', 'LISA', 'barT'];
def normalize(s):
	return s[0].upper()+s[1:].lower();
print map(normalize, frma);
#	['Adam', 'Lisa', 'Bart']

# filter
def not_empty(s):
    return s and s.strip();

print filter(not_empty, ['A', '', 'B', None, 'C', '  ']);
#	['A', 'B', 'C']

# sorted
sor = [36, 5, 12, 9, 21];
print sorted(sor)
#	[5, 9, 12, 21, 36]

def reversed_cmp(x, y):
    if x > y:
        return -1;
    if x < y:
        return 1;
    return 0;
print sorted(sor, reversed_cmp);
#	[36, 21, 12, 9, 5]

# lambda
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
#	[1, 4, 9, 16, 25, 36, 49, 64, 81]

# Decorator
def log(func):
    def wrapper(*args, **kw):
        print 'begin %s() function:' % func.__name__;
        res = func(*args, **kw);
        print 'end %s() function:' % func.__name__;
        return res;
    return wrapper;

import time;
@log
def now():
    print time.strftime('%Z : %Y-%m-%d %H:%M:%S = %x (%B-%A) %jrd days',time.localtime(time.time()));

now();
#	begin now() function:
#	CST : 2016-06-30 11:26:54 = 06/30/16 (June-Thursday) 182rd days
#	end now() function:

# wrapper.__name__ = func.__name__  / functools.wraps
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__);
            res = func(*args, **kw);
            print '%s %s() end' % (text, func.__name__);
            return res;
        return wrapper;
    return decorator;

@log('execute')
def now():
    print time.strftime('%Z : %Y-%m-%d %H:%M:%S = %x (%B-%A) %jrd days',time.localtime(time.time()));

now();
#	execute now():
#	CST : 2016-06-30 11:33:56 = 06/30/16 (June-Thursday) 182rd days
#	execute now() end

# Partial

print int('1000000');
#	1000000

import functools
int2 = functools.partial(int, base=2)
print int2('1000000');
#	64

