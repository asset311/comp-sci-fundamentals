'''
Write a program that takes as input a set of words and returns groups of anagrams for those words.
Each group must contain at least two words.
Example:
['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money']
1) 'debitcard', 'badcredit'
2) 'elvis', 'lives', 'levis'
3) 'silent', 'listen'
'money' has no anagram
'''

# two words are anagrams if and only if they result in equal strings after sorting
# use a hashtable, use sorted words as keys, and then append those words as values

import collections
def find_anagrams(dictionary):
    sorted_strings_to_anagrams = collections.defaultdict(list)

    for s in dictionary:
        # sorts the string, uses it as a key, and then appends to the original
        # string as another value into hashtable
        sorted_strings_to_anagrams[''.join(sorted(s))].append(s)
    
    return [ group for group in sorted_strings_to_anagrams.values() if len(group) >= 2 ]


'''
Complexity
sorting takes O(n m logm), where n is the number of strings, and m is maximum length string
insertion is O(n m)
so overall time complexity is O(n m logm)

'''


'''
Tests
'''

import unittest
class Test(unittest.TestCase):

    def test_valid_anagram(self):
        dictionary = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money']
        anagrams = [['debitcard', 'badcredit'], ['elvis', 'lives', 'levis'], ['silent', 'listen']]
        result = find_anagrams(dictionary)
        self.assertEqual(result.sort(), anagrams.sort())    #need to sort since ordering is not guaranteed

unittest.main(verbosity=2)