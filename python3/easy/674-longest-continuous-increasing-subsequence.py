#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (46.28%)
# Likes:    1362
# Dislikes: 151
# Total Accepted:    163.4K
# Total Submissions: 347.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an unsorted array of integers nums, return the length of the longest
# continuous increasing subsequence (i.e. subarray). The subsequence must be
# strictly increasing.
# 
# A continuous increasing subsequence is defined by two indices l and r (l < r)
# such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for
# each l <= i < r, nums[i] < nums[i + 1].
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with
# length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as
# elements 5 and 7 are separated by element
# 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length
# 1. Note that it must be strictly
# increasing.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 
        length = 1
        i = 1
        start = 0
        while i < len(nums):
            while i < len(nums) and nums[i - 1] < nums[i]:
                if nums[i] > nums[i - 1]:
                    length = max(length, i - start + 1)
                i += 1
            if i >= len(nums):
                return length
            start = i
            i += 1

        return length

# @lc code=end
