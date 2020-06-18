'''
An array is said to be cyclically sorted if it is possible to cyclically shift its entries so that it becomes sorted
A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
Returns 4 (103)
Design O(logn) algorithm for finding the position of the smallest element in a cyclically sorted array.
Assume all elements are distinct.
'''

# Brute force solution is to sequentially update running minimum, this runs in O(n)
def search_smallest(A):
    min_index = 0
    for i in range(1,len(A)-1):
        if A[i] < A[min_index]:
            min_index = i
    return min_index

# To design O(logn) solution, we need to use the structure of the array
# For any m, if A[m] > A[n-1] then the minimum value is in A[m+1, n-1]
# Conversely, if A[m] < A[n-1] then the minimum value cannot be in A[m+1, n-1]

def search_smallest(A):
    left, right = 0, len(A) - 1

    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid+1 : right+1]
            left = mid + 1
        else: # A[mid] < A[right]
            # Minimum cannot be in A[mid+1 : right + 1] so it must be in A[left:mid+1]
            right = mid
        #the loop ends when left = right
    
    return left