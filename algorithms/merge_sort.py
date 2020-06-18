'''
Classic merge sort algorithm for sorting elements in an array
O(n log n) is average, best and worst performance
'''

def mergeSort(A):
    #base case returns when array has 1 element
    if len(A) == 1:
        return
    
    if len(A) > 1:
        
        # partition part and recursive call
        # this is O(logn)
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        mergeSort(L)
        mergeSort(R)

        # merging part runs in O(n)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i, k = i+1, k+1

        while j < len(R):
            A[k] = R[j]
            j, k = j+1, k+1

# test worst-case scenario when the list is sorted in reverse order
import unittest
class Test(unittest.TestCase):
    def test_reversed_array(self):
        arr = list(range(20))
        arr.reverse()
        result = mergeSort(arr)
        self.assertEqual(arr, list(range(20)))

unittest.main(verbosity=2)
         

