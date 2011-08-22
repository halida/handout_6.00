#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps3b
"""
from string import *


def subStringMatchExact(target, key):
    i = find(target, key)
    if i >= 0:
        vs = subStringMatchExact(target[i+len(key):], key)
        new_vs = [v + i + len(key) for v in vs]
        new_vs.insert(0, i)
        return tuple(new_vs)
    else:
        return ()

def main():
    """
    >>> subStringMatchExact("atgacatgcacaagtatgcat","atgc") == (5, 15)
    True
    
    target1 = 'atgacatgcacaagtatgcat'
    target2 = 'atgaatgcatggatgtaaatgcag'

    key10 = 'a'
    key11 = 'atg'
    key12 = 'atgc'
    key13 = 'atgca'


    """
    import doctest
    doctest.testmod()
    
if __name__=="__main__":
    main()


