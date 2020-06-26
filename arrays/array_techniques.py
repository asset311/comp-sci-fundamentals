
'''
SLIDING WINDOWS
'''

# 1. For an array of size n and integer k, find maximum sum of any contiguous subarray of size k

# Brute-force solution
def find_max_subarray_sum(n: list, k: int) -> int:
    msum = 0
    i = 0
    while i<= len(n) - k:
        wsum = 0
        for j in range(i,i+k):
            wsum += n[j]
        if wsum >= msum:
            msum = wsum
        i += 1
    return msum

# Sliding window solution, the trick is that once an initial window sum is calculated
# the next window sum is simply dropping the first value and adding the next value
def find_max_subarray_sum(n:list, k:int) -> int:
    wsum = msum = 0
    for i in range(k):
        wsum += n[i]
    
    end = k
    while end < len(n):
        wsum += n[end] - n[end-k]
        msum = max(msum, wsum)
        end += 1
    
    return msum
