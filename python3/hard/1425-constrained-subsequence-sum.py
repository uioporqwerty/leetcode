#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#
# https://leetcode.com/problems/constrained-subsequence-sum/description/
#
# algorithms
# Hard (53.07%)
# Likes:    1854
# Dislikes: 92
# Total Accepted:    63K
# Total Submissions: 111.7K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subsequence of that array such that for every two consecutive
# integers in the subsequence, nums[i] and nums[j], where i < j, the condition
# j - i <= k is satisfied.
# 
# A subsequence of an array is obtained by deleting some number of elements
# (can be zero) from the array, leaving the remaining elements in their
# original order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest
# number.
# 
# 
# Example 3:
# 
# 
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
from heapq import *

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        ans = nums[0]
        heap = [(-nums[0], 0)]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heappop(heap)

            cur_max = max(nums[i], nums[i] - heap[0][0])
            ans = max(ans, cur_max)
            heappush(heap, (-cur_max, i))

        return ans
        # Below gets TLE
        # dp = [n for n in nums]
        
        # for i in range(1, len(nums)):
        #     for j in range(max(0, i - k), i):
        #         dp[i] = max(dp[i], nums[i] + dp[j])
        
        # return max(dp)
# @lc code=end
