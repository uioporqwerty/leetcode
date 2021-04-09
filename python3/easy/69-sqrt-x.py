#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (35.04%)
# Likes:    1916
# Dislikes: 2307
# Total Accepted:    705.7K
# Total Submissions: 2M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        result = -1
        while i <= j:
            mid = (i + j) >> 1
            if mid * mid <= x:
                result = mid
                i = mid + 1
            else:
                j = mid - 1

        return result


# @lc code=end
