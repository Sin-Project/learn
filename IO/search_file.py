#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def search_file(dir_name, keyword):
    for x in os.listdir(dir_name):
        x = os.path.join(dir_name, x);
        if os.path.isdir(x):
            search_file(x, keyword);
        if os.path.isfile(x):
            if keyword in os.path.splitext(os.path.split(x)[1])[0]:
                print os.path.join(dir_name, x);

if len(sys.argv) != 2:
    print "Please give the keyword, like:\"python search_file.py keyword\"";
    sys.exit();
keyword = sys.argv[1];
dir_name = os.path.abspath('.');
search_file(dir_name, keyword);