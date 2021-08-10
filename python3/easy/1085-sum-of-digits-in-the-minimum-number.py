#
# @lc app=leetcode id=1085 lang=python3
#
# [1085] Sum of Digits in the Minimum Number
#
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/description/
#
# algorithms
# Easy (75.50%)
# Likes:    63
# Dislikes: 126
# Total Accepted:    17.8K
# Total Submissions: 23.6K
# Testcase Example:  '[34,23,1,24,75,33,54,8]'
#
# Given an integer array nums, return 0 if the sum of the digits of the minimum
# integer in nums is odd, or 1 otherwise.
#
#
# Example 1:
#
#
# Input: nums = [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: The minimal element is 1, and the sum of those digits is 1 which
# is odd, so the answer is 0.
#
#
# Example 2:
#
#
# Input: nums = [99,77,33,66,55]
# Output: 1
# Explanation: The minimal element is 33, and the sum of those digits is 3 + 3
# = 6 which is even, so the answer is 1.
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
    def getSum(self, n: int) -> int:
        total = 0
        while n:
            total += n % 2
            n //= 10
        return total

    def sumOfDigits(self, nums: List[int]) -> int:
        min_digit = min(nums)
        total = self.getSum(min_digit)
        return 1 if total % 2 == 0 else 0


# @lc code=end
