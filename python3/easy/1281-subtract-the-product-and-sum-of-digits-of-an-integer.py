#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
#
# algorithms
# Easy (85.56%)
# Likes:    491
# Dislikes: 131
# Total Accepted:    132.8K
# Total Submissions: 155.1K
# Testcase Example:  '234'
#
# Given an integer number n, return the difference between the product of its
# digits and the sum of its digits.
#
# Example 1:
#
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
#
#
# Example 2:
#
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits_product = 1
        digits_sum = 0
        while n:
            digit = n % 10
            digits_product *= digit
            digits_sum += digit
            n //= 10

        return digits_product - digits_sum


# @lc code=end
