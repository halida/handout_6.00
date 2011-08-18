#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps1b
"""
from math import *

def process(n):
    result = log(2) + log(3)

    for v in range(4, n):
        for i in range(2, v):
            if v % i == 0:
                break
        else:
            result += log(v)

    print n, ": ", result, ": ", result/float(n)
    return n

for i in range(11, 20000):
    process(i)

