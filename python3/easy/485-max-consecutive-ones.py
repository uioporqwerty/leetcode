#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (52.95%)
# Likes:    1091
# Dislikes: 380
# Total Accepted:    354.8K
# Total Submissions: 670.1K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_consecutive_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current_consecutive_count = 0
            else:
                current_consecutive_count += 1
                max_ones = max(max_ones, current_consecutive_count)

        return max_ones


# @lc code=end
