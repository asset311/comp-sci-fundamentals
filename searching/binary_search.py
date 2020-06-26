
def binary_search(A, target):
    L, U = 0, len(A)-1
    while L <= U:
        M = (L + U) // 2    #this will avoid overflow for very large arrays
        if A[M] < target:
            L = M + 1
        elif A[M] == target:
            return M
        else:
            U = M - 1
    return -1