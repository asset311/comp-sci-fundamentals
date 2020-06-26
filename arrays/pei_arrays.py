'''
TIPS:
1. Try to use the array itself, to not introduce additional O(n) space complexity
2. Try to fill values from the back, as writing from the front is slow
3. Instead of deleting a value, try overwriting (so the array doesn't shift left)
4. Operate on subarrays
5. Do not go over the border (BufferOverFlow in Java)
6. When operating on 2D arrays, use parallel logic to work on rows and columns

METHODS:
list() is the construct for an array
range(x,y)  - generate a list [a,b)
len(A)      - number of elements in A
A.append(x) - add single value to the end of the list
A.extend(B) - extend the list with the individual values from B
A.remove(x) - remove first matching x from the list
A.insert(3,x) - insert x at position 3
A.index(x)  - returns the index of the first occurence of x in the list
A.count(x)  - returns the number of times x occurs in the list
A.pop(x)    - removes x at the given index from the list and returns the removed item.
                If no index, then removes at -1.
A.reverse() - reverses the elements of the list. Updates in-place
A.sort()    - sorts the list. Updates in-place
sorted(A)   - returns a new list that is a sorted A
A.copy()    - returns a shallow copy of A
'''

'''
EXERCISES:

Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
'''
# start a opposite ends and swap values as two pointers are moving towards each other
# the array is passed by reference, hence there is no copying and the original array is changed
# additonal space complexity is O(1) for a couple of vars holding indices
# there is a constant time for performing the swap, so the time complexity is O(n)
def even_odd(A):
    next_even, next_odd = 0, len(A)-1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even +=1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -=1

'''
    5.2 Increment an arbitrary-precision integer    
Write a program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.  
Your algorithm should work even if it is implemented in a langua ge that has finite-precision arithmetic.
Examples:
(1,2,9) -> (1,3,0)
(2,9,9) -> (3,0,0)
(9,9) -> (1,0,0)
'''
# brute-force solution: convert the array of digits to the equivalent integel, increment that, and then convert the resulting value back to an array of digits.
# when implemented in a language that imposes a limit on the range of values an integer can take, this will fail on large inputs
def convert_digits_int(numList):
    s = map(str, numList)
    s = ''.join(s)
    return int(s)    #one-liner return int(''.join(map(str,numList)))

def convert_int_digits(num):
    s = list(str(num))
    return list(map(int,s))

def plus_one(A):
    num = 1 + convert_digits_int(A)
    return convert_int_digits(num)

# user high-school addition method with carry
# this will not fail because of limitations on the integer storage, like the brute-force solution
# complexity is O(n) where n is the length of A
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:  #if there is a carry-out then we need to add 1 at the front, and append 0
        A[0] = 1
        A.append(0)
    return A

'''
    5.5 Delete duplicates from a sorted array
This problem is concerned with deleting repeated elements from a sorted array. 
For example, for the array <2,3,5,5,7,1.1.,L1.,77,73>, then after deletion, the array is (2,3,5,7,77,73,0,0,0).
'''
# A fast solution is to convert to a set, then convert back to an array
# Space complexity O(n) and time complexity is O(n)
def delete_duplicates(A):
    return  list(set(A))

# Additional constraint is to not use the array itself without using additional libraries
# Also take advantage that the array is sorted, so only immediate neighbours can be duplicates
# We need to minimize shifting to achieve good time complexity
# Time complexity O(n) and space complexity O(1)
def remove_duplicates(A) -> None:
    A.sort()    #make sure duplicates are adjacent
    write_index = 1
    for cand in A[1:]:  #an array of the actual values
        if cand != A[write_index - 1]:
            A[write_index] = cand
            write_index+=1
    del A[write_index:]

def remove_duplicates(A) -> None:
    A.sort()
    write_index = 1
    for i in range(1,len(A)):
        if A[i] != A[write_index-1]:    #needs to access the actual value from the array O(1)
            A[write_index] = A[i]
            write_index += 1
    del A[write_index:]

# a pythonic implementation leverages itertools library - functional programming style
# groupby creates pairs of (key, group) so we can just extract the keys
import itertools
def remove_duplicates(A) -> None:
    A.sort()
    write_index = 0
    for cand, _ in itertools.groupby(A):
        A[write_index] = cand
        write_index += 1
    del A[write_index:]


'''
5.14 Computer a random permutation
Design an algorithm that creates a uniformly random permutations of [0,1,...,n-1].
You are given a random number generator that returns integers in the set {0,1,...,n-1} with equal probability.
Use as few calls to it as possible.
'''
import math

#test data
partial_assignment = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# this will individually test for a duplicate constraint
# returns true if there is a duplicate
def has_duplicate(block):
    #filter all the zeroes first
    block = list(filter(lambda x: x != 0, block))
    return len(block) != len(set(block))

# We directly check 9 row constraints, 9 column constraints, and 9 sub-grid constraints
def is_valid_sudoku(partial_assignment):

    n = len(partial_assignment)     #number of rows and columns is equal

    #this runs through rows and cols
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False
    
    #this checks quadrant regions
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size*I, region_size*(I+1))
        for b in range(region_size*J, region_size*(J+1))
    ]) for I in range(region_size) for J in range(region_size))

# time complexity is O(n^2) + O(n^2) to check n rows and n cols
# + O(n^2) to check sub-grids
# so the total time complexity is O(n^2)
# space complexity is allocation of bits arrays which is O(n)


