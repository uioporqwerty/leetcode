#
# @lc app=leetcode id=1133 lang=python3
#
# [1133] Largest Unique Number
#
# https://leetcode.com/problems/largest-unique-number/description/
#
# algorithms
# Easy (67.27%)
# Likes:    198
# Dislikes: 15
# Total Accepted:    26.3K
# Total Submissions: 39.1K
# Testcase Example:  '[5,7,3,9,4,9,8,3,1]'
#
# Given an integer array nums, return the largest integer that only occurs
# once. If no integer occurs once, return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The
# number 8 occurs only once, so it is the answer.
# 
# Example 2:
# 
# 
# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        i, j = len(nums) - 1, len(nums) - 1
        while i >= 0:
            while j >= 0 and nums[i] == nums[j]:
                j -= 1
                
            if i - j > 1:
                i = j
            else:
                return nums[i]

        return -1 
# @lc code=end
