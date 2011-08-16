#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps1a_2
"""
count = 2
v = 3

while count < 1000:
    for i in range(2, v):
        if v % i == 0:
            break
    else:
        count += 1
    v += 2
print v
