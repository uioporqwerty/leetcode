#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#
# https://leetcode.com/problems/armstrong-number/description/
#
# algorithms
# Easy (77.77%)
# Likes:    129
# Dislikes: 15
# Total Accepted:    24.2K
# Total Submissions: 30.7K
# Testcase Example:  '153'
#
# Given an integer n, return true if and only if it is an Armstrong number.
#
# The k-digit number n is an Armstrong number if and only if the k^th power of
# each digit sums to n.
#
#
# Example 1:
#
#
# Input: n = 153
# Output: true
# Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
#
#
# Example 2:
#
#
# Input: n = 123
# Output: false
# Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^8
#
#
#

# @lc code=start
import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        original = n
        armstrong_sum = 0
        total_digits = math.floor(math.log10(n)) + 1
        while original:
            digit = original % 10
            armstrong_sum += digit ** total_digits
            original //= 10

        return armstrong_sum == n


# @lc code=end
