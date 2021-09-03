#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (60.15%)
# Likes:    723
# Dislikes: 96
# Total Accepted:    81K
# Total Submissions: 134.1K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# 
# Example 1:
# 
# 
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# 
# 
# Example 2:
# 
# 
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# 
# Example 3:
# 
# 
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
# 
# Example 4:
# 
# 
# Input: n = 10
# Output: true
# Explanation: The binary representation of 10 is: 1010.
# 
# Example 5:
# 
# 
# Input: n = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        previous_bit = None

        while n:
            if previous_bit is not None and previous_bit == n & 1:
                return False
            previous_bit = n & 1
            n >>= 1
        
        return True

# @lc code=end
