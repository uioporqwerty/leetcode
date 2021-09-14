#
# @lc app=leetcode id=1056 lang=python3
#
# [1056] Confusing Number
#
# https://leetcode.com/problems/confusing-number/description/
#
# algorithms
# Easy (46.76%)
# Likes:    134
# Dislikes: 86
# Total Accepted:    20.7K
# Total Submissions: 44.6K
# Testcase Example:  '6'
#
# A confusing number is a number that when rotated 180 degrees becomes a
# different number with each digit valid.
# 
# We can rotate digits of a number by 180 degrees to form new digits.
# 
# 
# When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6
# respectively.
# When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
# 
# 
# Note that after rotating a number, we can ignore leading zeros.
# 
# 
# For example, after rotating 8000, we have 0008 which is considered as just
# 8.
# 
# 
# Given an integer n, return true if it is a confusing number, or false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: n = 6
# Output: true
# Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
# 
# 
# Example 2:
# 
# 
# Input: n = 89
# Output: true
# Explanation: We get 68 after rotating 89, 86 is a valid number and 86 !=
# 89.
# 
# 
# Example 3:
# 
# 
# Input: n = 11
# Output: false
# Explanation: We get 11 after rotating 11, 11 is a valid number but the value
# remains the same, thus 11 is not a confusing number
# 
# 
# Example 4:
# 
# 
# Input: n = 25
# Output: false
# Explanation: We get an invalid number after rotating 25.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid_rotations = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        original_num = n
        rotated_num = 0
        while n:
            digit = n % 10
            if digit not in valid_rotations:
                return False
            rotated_digit = valid_rotations[digit]
            rotated_num = 10 * rotated_num + rotated_digit
            n //= 10
            
        return rotated_num != original_num
# @lc code=end
