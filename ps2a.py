#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# Problem Set 2 (Part I)
# Name: halida
# Time: 00:30 (about that time)
#
"""
module: ps2a
"""
def test(n):
    """
    test if n in Set(Mc)
    """
    for i in range(n/6 + 1):
        for j in range(n/9 + 1):
            for k in range(n/20 + 1):
                if n == i * 6 + j * 9 + k * 20:
                    return True

def find_largest():
    i = 5
    failed = 5
    continue_n = 0
    while continue_n < 6:
        i += 1
        if test(i):
            continue_n += 1
        else:
            continue_n = 0
            failed = i
    print "Largest number of McNuggets that cannot be bought in exact quantity: %d" % failed

def find_set(x, y, z):
    def test(n):
        for i in range(n/x + 1):
            for j in range(n/y + 1):
                for k in range(n/z + 1):
                    if n == i * x + j * y + k * z:
                        return True
    i = 0
    failed = -1
    continue_n = 0
    while continue_n < min(x, y, z):
        i += 1
        if test(i):
            continue_n += 1
        else:
            continue_n = 0
            failed = i
    print "Given package sizes %d, %d, and %d, the largest number of McNuggets that cannot be bought in exact quantity is: %d" % (x, y, z, failed)


def main():
    # print test(58) # True
    # find_largest() # 43
    find_set(6, 9, 20)
    
if __name__=="__main__":
    main()
