#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: ps3d
Time: 00:08
"""
from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def subStringMatchExact(target, key):
    if len(key) <= 0: return ()
    i = find(target, key)
    if i >= 0:
        vs = subStringMatchExact(target[i+len(key):], key)
        new_vs = [v + i + len(key) for v in vs]
        new_vs.insert(0, i)
        return tuple(new_vs)
    else:
        return ()


### the following procedure you will use in Problem 3
def constrainedMatchPair(firstMatch, secondMatch, length):
    if len(firstMatch) <= 0:
        firstMatch = range(max(secondMatch))
    if len(secondMatch) <= 0:
        secondMatch = range(max(firstMatch))
    i = 0
    j = 0
    m = length
    answers = ()
    while i < len(firstMatch) and j < len(secondMatch):
        n = firstMatch[i]
        k = secondMatch[j]
        if n + m + 1 > k:
            j += 1
        elif n + m + 1 < k:
            i += 1
        else:
            answers = answers + (firstMatch[i],)            
            i += 1
            j += 1
    return answers

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers


def subStringMatchExactlyOneSub(key, target):
    perfacts = subStringMatchExact(target, key)
    ones = subStringMatchOneSub(key, target)
    values = [i
              for i in ones
              if i not in perfacts]
    return values
        

def main():
    print subStringMatchExactlyOneSub(key12, target1)
    
if __name__=="__main__":
    main()

