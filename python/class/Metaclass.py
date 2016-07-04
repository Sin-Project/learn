#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' python class '''

__author__ = 'Michael Liao';

# metaclass is createclass, must be from type
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value);
        return type.__new__(cls, name, bases, attrs);

class MyList(list):
    __metaclass__ = ListMetaclass; # use ListMetaclass creat class

L = MyList();
L.add(1000);
print L;
#   [1000]

#   l = list();
#   l.add(1000);
#   AttributeError: 'list' object has no attribute 'add'


# ORM framework
# emp: User 
        # class User(Model):
        #     # field：
        #     id = IntegerField('id')
        #     age = IntegerField('age')
        #     name = StringField('username')
        #     email = StringField('email')
        #     password = StringField('password')

        # 
        # u = User(id=12345, age=55, name='mike', email='test@orm', password='pwd')
        # save to database
        # u.save()

class Field(object):
    def __init__(self, name, column_type):
        self.name = name;
        self.column_type = column_type;

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name);

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(255)');

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint');


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs);
        print 'Found model: %s' % name;
        mappings = dict();
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v));
                mappings[k] = v;
        for k in mappings.iterkeys():
            attrs.pop(k);
        attrs['__table__'] = name; # class name = table name
        attrs['__mappings__'] = mappings; # Relational Mapping
        return type.__new__(cls, name, bases, attrs);


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw);

    def __getattr__(self, key):
        try:
            return self[key];
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key);

    def __setattr__(self, key, value):
        self[key] = value;

    def save(self):
        fields = [];
        params = [];
        args = [];
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name);
            params.append(str(getattr(self, k, None)));
            args.append(getattr(self, k, None));
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params));
        print('SQL: %s' % sql);
        print('ARGS: %s' % str(args));

class User(Model):
    """docstring for User"""
    uid = IntegerField('uid');
    age = IntegerField('age');
    name = StringField('username');
    email = StringField('email');
    password = StringField('password');

u = User(uid = 22, age = 32, name = 'sa', email = 'sadd', password = 'sssss');
u.save();