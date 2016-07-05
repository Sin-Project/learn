#!/usr/bin/env python
# -*- coding: utf-8 -*-

# namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']);
coordinate = Point(33, 231);
print coordinate.x ,coordinate.y;
#	33 231
Circle = namedtuple('Circle', ['x', 'y', 'r']);

# deque
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q
#	deque(['y', 'a', 'b', 'c', 'x'])

# defaultdict
from collections import defaultdict;
dd = defaultdict(lambda: 'N/A');
dd['key1'] = 'abc';
print dd['key1'];
#	'abc'
print dd['key2'];
#	'N/A'

# orderedDict
from collections import OrderedDict;
d = dict([('a', 1), ('b', 2), ('c', 3)]);
print d;
#	{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)]);
print od;
#	OrderedDict([('a', 1), ('b', 2), ('c', 3)]);

od = OrderedDict();
od['z'] = 1;
od['y'] = 2;
od['x'] = 3;
print od.keys() ;
#	['z', 'y', 'x']

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__();
        self._capacity = capacity;

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0;
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False);
            print 'remove:', last;
        if containsKey:
            del self[key];
            print 'set:', (key, value);
        else:
            print 'add:', (key, value);
        OrderedDict.__setitem__(self, key, value);

# counter
from collections import Counter;
c = Counter();
for ch in 'programming':
     	c[ch] = c[ch] + 1;
print c
#	Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})