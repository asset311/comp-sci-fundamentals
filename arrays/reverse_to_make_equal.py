'''
REVERSE TO MAKE EQUAL
Given two arrays A and B of length N, 
determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
'''

# This is an example of an anagram - a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
# This reduces to answering if any permutation of array_b is equal to array_a

# I have two solutions, one involving constructing dictionaries and directly comparing
# the second involves creating sets and directly comparing

import math
import itertools

# space and time complexity is O(n) 
def are_they_equal_dict(array_a, array_b):
    # trivial cases
    if len(array_a) != len(array_b):
        return False
    if array_a == array_b:
        return True
    
    # create dictionaries using itertools groupby
    # both arrays need to be sorted first
    dict_a = {k:list(g) for k,g in itertools.groupby(array_a.sort())}
    dict_b = {k:list(g) for k,g in itertools.groupby(array_b.sort())}

    for key in dict_a.keys():
        if dict_a.get(key) != dict_b.get(key):  #if array_b does not contain this key, it will return None
            return False
    
    return True

# more trivial solution?
def are_they_equal_sort(array_a, array_b):
    return sorted(array_b) == sorted(array_a)

