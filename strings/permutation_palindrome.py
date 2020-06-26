'''
Check if any permutation of a string is a valid palindrome.

A brute force approach is to generate all permutations of the string = O(n!)
Then for each of those permutations to check if it is a palindrome = 0(n)
For the total time of O(n*n!) - that's extremely long.

A simple solution is to think about what a palindrome is.
In a palindrome, each letter needs to appear even number of times, except maybe one appearing odd number of times.
Our approach is to check that each character appears an even number of times, allowing for only one character to appear an odd number of times (a middle character). 
This is enough to determine if a permutation of the input string is a palindrome.
'''

# O(n) time complexity
# O(1) space for possible characters added to the set
def has_palindrome_permutation(the_string):
    #track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)
    
    # the string has a palindrome permutation if it
    # has one or zero characters without a pair
    return (len(unpaired_characters)) <= 1