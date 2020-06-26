'''
325. Maximum sum of contiguous subarray of size k
Given an array of integers n and a positive number k,
find the maximum sum of any contiguous subarray of size k

Example
Input: [2,1,5,1,3,2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5,1,3]
'''

# We use a sliding window technique, since the size of the window is fixed
# this runs in O(n) and space O(1)
def maxSum(numbers:list, k:int) -> int:
    mSum = wSum = 0

    #find the sum of initial window of size k
    #for i in numbers[:k]:
    #    wSum += i
    wSum = sum(numbers[:k])

    end = k
    while end < len(numbers):
        wSum += numbers[end] - numbers[end-k]
        mSum = max(mSum, wSum)
        end +=1
    return mSum


# We can also use a two-pointer technique
def maxSum(numbers:int, k:int) -> int:
    mSum = wSum = 0
    start = end = 0

    #find the sum of initial window of size k
    for i in numbers[:k]:
        wSum += i
        end +=1
    
    while end < len(numbers):
        wSum += numbers[end] - numbers[start]
        start, end = start+1, end+1
        mSum = max(wSum, mSum)
    return mSum