#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps3a
"""
from string import *

def countSubStringMatch(target, key):
    i = 0
    k = 0
    while i != -1:
        i = find(target, key, i)
        if i < 0: break
        i += len(key)
        k += 1
    return k

def countSubStringMatchRecursive(target, key):
    i = find(target, key)
    if i >= 0:
        return 1 + countSubStringMatchRecursive(target[i+len(key):], key)
    else:
        return 0


def main():
    """
    >>> countSubStringMatch('abcdfaacc', 'a') == 3
    True
    >>> countSubStringMatchRecursive('abcdfaacc', 'a') == 3
    True
    """
    import doctest
    doctest.testmod()
    
if __name__=="__main__":
    main()


