#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image;

im = Image.open('/Users/magce.qin/Documents/fff.jpeg');

w, h = im.size;
print w;
print h;
newsize = (w//2, h//2);
im.thumbnail(newsize);

im.save('/Users/magce.qin/Documents/thumbnail.jpeg', 'jpeg');

import ImageFilter,

im = Image.open('/Users/magce.qin/Documents/fff.jpeg')
im2 = im.filter(ImageFilter.BLUR) # vague
im2.save('/Users/magce.qin/Documents/fff.jpeg', 'jpeg');

