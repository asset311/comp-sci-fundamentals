'''
Implementation of the classic quick sort algorithm
Worst case performance is O(n^2)
Best and average performance is O(nlogn)
'''

# user interface, just a wrapper
def quick_sort(A):
    quick_sort_recursive(A, 0, len(A)-1)

def quick_sort_recursive(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)   #this will return a pivot index
        quick_sort_recursive(A, low, p-1)
        quick_sort_recursive(A, p+1, hi)


def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]   #swap the pivot and the value at low end
    border = low

    # i is the scanner index
    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
        A[low], A[border] = A[border], A[low]
    return border

# essentially performs a calculation of the pivot that points to median
def get_pivot(A, low, hi):
    mid = (low + hi) // 2
    pivot = hi

    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = hi
    
    return pivot


# a much simpler impementation that is very not memory efficient, since it creates new lists at each recursion call
# quick sort needs to be sorting in place without allocating additional arrays
def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)