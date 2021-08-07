#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#
# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
#
# algorithms
# Easy (64.62%)
# Likes:    247
# Dislikes: 9
# Total Accepted:    20.8K
# Total Submissions: 32.3K
# Testcase Example:  '[10,20,30,5,10,50]'
#
# Given an array of positive integers nums, return the maximum possible sum of
# an ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
# where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is
# ascending.
#
#
# Example 1:
#
#
# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of
# 65.
#
#
# Example 2:
#
#
# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum
# of 150.
#
#
# Example 3:
#
#
# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of
# 33.
#
#
# Example 4:
#
#
# Input: nums = [100,10,1]
# Output: 100
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        curr_sum = nums[0]

        for window_end in range(1, len(nums)):
            if nums[window_end] <= nums[window_end - 1]:
                curr_sum = nums[window_end]
            else:
                curr_sum += nums[window_end]

            max_sum = max(max_sum, curr_sum)
        return max_sum


# @lc code=end
