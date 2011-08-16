#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps1a
"""
def main():
    primes = [2, 3]
    i = 3
    while len(primes) < 1000:
        i += 2
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    print primes[1000-1]
    
if __name__=="__main__":
    main()
