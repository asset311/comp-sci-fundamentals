'''
Write a method that takes a sorted array and a key and returns the index of the first occurrence
of that key in the array. Return -1 if the key doesn't appear in the array.

Example:
[-14,-10,2,108,108,243,285,285,285,401]

Returns 3 if key = 108
Returns 6 if key = 285
'''

def search_first_of_k(A, k):
    left, right, result = 0, len(A)-1, -1
    
    # the candidate set is A[left:right+1]
    while left <= right:
        mid = (left+right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1 # nothing to the right of mid can be a solution
        else:
            left = mid + 1
    return result