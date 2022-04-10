#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.74%)
# Likes:    2145
# Dislikes: 228
# Total Accepted:    350.2K
# Total Submissions: 815.2K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        i, j = 2, num // 2

        while i <= j:
            guess = (i + j) // 2
            guess_squared = guess * guess

            if guess_squared == num:
                return True
            elif guess_squared > num:
                j = guess - 1
            else:
                i = guess + 1
        
        return False


# @lc code=end
