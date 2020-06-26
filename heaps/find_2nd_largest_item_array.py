
# A heap is a good choice when you need to compute the k largest or k smallest elements in a collection
import heapq
def find_2nd_largest(A):
    return (heapq.nlargest(2,A))[-1]

# the way it works behind the scenes is
# negate all the numbers in the list first
# heapq.heapify(A) - will transform into min-heap in-place
# return the first two min elements, and then negate back

# solution using two pointers

def find_2nd_largest(A):
    first_max = -float('inf')
    second_max = -float('inf')

    for i in range(len(A)):
        if A[i] > first_max:
            second_max = first_max
            first_max = A[i]
        elif A[i] > second_max:
            if A[i] != first_max:
                second_max = A[i]
    
    return second_max



'''
Tests
'''
import unittest
class Test(unittest.TestCase):

    def test_increasing_array(self):
        array = range(10)
        result = find_2nd_largest(array)
        self.assertEqual(result, 8)

    def test_with_repeated_entries(self):
        array = [-1,10,8,9,10,-8,9,11]
        result = find_2nd_largest(array)
        self.assertEqual(result, 10)

unittest.main(verbosity=2)