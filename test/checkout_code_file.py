#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import re
source = """
def hello():    
    # 
    print()
    def hel():
        asd

def hell(): 
    pass
    

"""


indentation_key = ['    ', "\t"]


def hello(source):
    """
    :return: list
    """
    split_list = source.split("\n")
    remove_empty = [y.rstrip() for y in [x for x in split_list if x] if '#' not in y]
    def_list = []
    for i in remove_empty:
        if i.startswith('def'):
            re.sub('\((.*)\):', '', 'def hello(asd):')
            now_dic = {i: []}
            def_list.append(now_dic)
        else:
            list(def_list[-1].values())[0].append(i)

    print(def_list)

hello(source)
