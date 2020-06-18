
'''
Search a sorted array for entry equal to its index

Design an efficient algorithm that takes a sorted array of distinct integers,
and returns an index i such that the element at i is equal to i.

For example
A = [-2, 0, 2, 3, 6, 7, 9]
returns 2 or 3
'''

# Notice that we can search a different array that is the difference
# between the value and its index. Then we reduce it to binary search for value 0

def search_entry_equal_to_its_index(A):
    left, right, result = 0, len(A)-1, -1
    while left <= right:
        mid = (left+right) // 2
        difference = A[mid] - mid
        # A[mid] == mid if and only if difference == 0
        if difference > 0:
            right = mid - 1
        elif difference == 0:
            return mid
        else:
            left = mid + 1
    return result