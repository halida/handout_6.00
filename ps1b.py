#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps1b
"""
from math import *

def process(n):
    count = 2
    v = 3
    result = log(2) + log(3)

    while count < n:
        for i in range(2, v):
            if v % i == 0:
                break
        else:
            count += 1
            result += log(v)
        v += 1

    print n, ": ", result
    return n

x = range(11, 200)
y = [process(i)
     for i in range(11, 200)]

import numpy as np
import matplotlib.pyplot as plt

plt.plot(x, y)
