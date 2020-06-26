'''
TIPS
- Strings are immutable, hence any concatenation creates a new string
- It is possible to have solutions that use strings themselves to have O(1) space complexity
- Updating a mutable string from the front is slow, so write values from the back
'''

'''
METHODS
string.strip([chars])   - removes characters from both left and right based on the argument
string.split(char)      - tokenizes the string based on the character, space by default
','.join([])            - joins strings with a character specified
'Name: {name}, Rank: {rank}'.format(name='Asset', rank='general') 
'''

'''
Efficient implementation of the palidrome
Operates with time complexity of O(n) and space complexity O(1) 
'''
def palidrome(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))   #read from opposite sides, and use complement


'''
6.1 Interconvert strings and integers
'''
def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    
    return ('-' if is_negative else '') + ''.join(reversed(s))

'''
6.5 Test palindromicity
For the purpose of this problem, define a palindromic string to be a string 
which when all the nonalphanumeric are removed it reads the same front to back ignoring case
Test
'A man, a plan, a canal, Panama.'
'Able was I, ere I saw Elba!'
'''

# naive implementation removes non-alphanumeric characters, reverses the string and performs a comparison
# this requires additional space proportional to the size of s
def remove_nonalnum(s):
    new_s = []
    i = 0
    while i < len(s)-1:
        if s[i].isalnum():
            new_s.append(s[i])
            i += 1
        else:
            i += 1
    return ''.join(new_s)
        
def is_palindrome_naive(s):
    new_s = (remove_nonalnum(s)).lower()
    return new_s == ''.join(reversed(new_s))

# Directly test going from two ends of the string, but making sure to not compare nonalphanumeric
# Space complexity is O(1) and time complexity is O(n)
def is_palindrome(s):
    #i moves forward, j moves backwards
    i, j = 0, len(s)-1
    while i<j:
        while not s[i].isalnum() and i<j:
            i += 1
        while not s[j].isalnum() and i<j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+1, j-1
    return True


'''
6.6 Reverse all the words in a sentence
Given a string containing a set of words separated by whitespace, 
we would like to transform it to a string in which the words appear in the reverse order.
'''

# Naive implementation is to reverse the original string, and each individual word
def reverse_words_naive(s):
    reversed_s = ''.join(reversed(s))
    return ' '.join([''.join(reversed(w)) for w in reversed_s.split()])

# pythonic version, also doesn't reverse in-place
def reverse_words_pythonic(s):
    return ' '.join(reversed(s.split()))


# reversing in place, thus reducing space complexity
# time complexity is O(n) and space complexity is O(1)
def reverse_words(obj):
    s = list(obj)   # first need to convert to an array of characters fo write in-place
    def reverse_range(s, start, finish):
        while start < finish:
            s[start],s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1
    
    # First reverse the whole string
    reverse_range(s, 0, len(s)-1)

    # reverse each individual word
    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != ' ':
            finish += 1
        # exit the loop once we reach end of the string
        if finish == len(s):
            break
        # reverses each word in a string
        reverse_range(s, start, finish - 1)
        start = finish + 1
    
    # reverses the last word
    reverse_range(s, start, len(s)-1)
    return ''.join(s)
