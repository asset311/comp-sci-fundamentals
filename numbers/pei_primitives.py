'''
4.8 Reverse digits
Write a program which takes an integer and returns the integer corresponding to the digits of the input written in reverse order. 
For example, the reverse of 42is 24, and the reverse of -314 is -413
'''

#brute force algorithm - convert into a string, reverse the list, and convert back into an int noting the sign
def reverse(x):
    s = str(abs(x))
    rev_s = list(reversed(list(s)))
    new_s = ''
    for i in rev_s:
        new_s +=i
    new_x = int(new_s)
    return -new_x if x<0 else new_x 

# we can avoid converting into a string if we instead modulo the result and work iteratiely backwards
# the complexity is O(n) where n is the number of digits in the input
def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result*10 + x_remaining % 10
        x_remaining //= 10
    return -result if x<0 else result


'''
4.1 Computer parity of a word
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
'''

#brute force is to compute the number of 1s in the input, and then check if it odd or even
