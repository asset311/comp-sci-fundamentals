''' 
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''
# sub-optimal solution is to find all subarrays, and find the max sum
def max_k_subarray_sum(l:list, k:int) -> int:
    #use sliding windows
    msum = wsum = 0
    for i in range(k):
        wsum += l[i]
    
    end = k
    while end < len(l):
        wsum += l[end] - l[end-k]
        msum = max(msum, wsum)
        end += 1
    return msum

def max_subarray_sum(l:list) -> int:
    msum = wsum = 0
    k = 1
    while k < len(l):
        wsum = max_k_subarray_sum(l, k)
        msum = max(wsum, msum)
        k += 1
    return msum

# optimal solution that runs in O(n)
# n = (-2,1,-3,4,-1,2,1,-5,4)
# Kadane's algorithm is able to find the maximum sum of a contiguous subarray in an array with a runtime of O(n)
def maxSubArray(nums) -> int:
    total_sum = max_sum = nums[0]

    for i in nums[1:]:
        total_sum = max(i, total_sum + i)
        max_sum = max(max_sum, total_sum)
    
    return max_sum