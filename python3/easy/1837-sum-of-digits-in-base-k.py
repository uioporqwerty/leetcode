#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#
# https://leetcode.com/problems/sum-of-digits-in-base-k/description/
#
# algorithms
# Easy (75.04%)
# Likes:    175
# Dislikes: 16
# Total Accepted:    19.7K
# Total Submissions: 26.2K
# Testcase Example:  '34\n6'
#
# Given an integer n (in base 10) and a base k, return the sum of the digits of
# n after converting n from base 10 to base k.
#
# After converting, each digit should be interpreted as a base 10 number, and
# the sum should be returned in base 10.
#
#
# Example 1:
#
#
# Input: n = 34, k = 6
# Output: 9
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
#
#
# Example 2:
#
#
# Input: n = 10, k = 10
# Output: 1
# Explanation: n is already in base 10. 1 + 0 = 1.
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 2 <= k <= 10
#
#
#

# @lc code=start
from math import floor, log, log10


class Solution:
    def sumDigits(self, n: int) -> int:
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total

    def convertToBase(self, n: int, base: int) -> int:
        power = int(log(n, base))
        converted = 0
        for pow in range(power, -1, -1):
            converted += (10 ** pow) * (n // (base ** pow))
            n %= base ** pow

        return converted

    def sumBase(self, n: int, k: int) -> int:
        converted = self.convertToBase(n, k)
        return self.sumDigits(converted)


# @lc code=end
