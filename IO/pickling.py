#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import cPickle as pickle;
except ImportError:
    import pickle;

d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d) # serialization
#	(dp1S'age'p2I20sS'score'p3I88sS'name'p4S'Bob'p5s.

f = open('dump.txt', 'wb');
pickle.dump(d, f); # save in the file
f.close();

f = open('dump.txt', 'rb');
result = pickle.load(f);
f.close();
print result;
#	{'age': 20, 'score': 88, 'name': 'Bob'}


# JSON
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d) # return str  ( 'json.dump' is save in file)
#	'{"age": 20, "score": 88, "name": "Bob"}'

# json class
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict)); # json type

print(json.dumps(s, default=lambda obj: obj.__dict__)); # any class to dict

# json to class
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
#	<__main__.Student object at 0x10cd3c190>