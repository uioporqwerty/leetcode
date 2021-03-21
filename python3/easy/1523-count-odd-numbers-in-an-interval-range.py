#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
#
# algorithms
# Easy (54.59%)
# Likes:    197
# Dislikes: 22
# Total Accepted:    21.4K
# Total Submissions: 39.3K
# Testcase Example:  '3\n7'
#
# Given two non-negative integers low and high. Return the count of odd numbers
# between low and high (inclusive).
#
#
# Example 1:
#
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
#
# Example 2:
#
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
#
# Constraints:
#
#
# 0 <= low <= high <= 10^9
#
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total_numbers = high - low + 1
        if total_numbers % 2 == 0:
            return total_numbers // 2
        else:
            if low % 2 != 0 or high % 2 != 0:
                return (total_numbers // 2) + 1
            else:
                return total_numbers // 2


# @lc code=end
