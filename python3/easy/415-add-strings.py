#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (51.36%)
# Likes:    2994
# Dislikes: 531
# Total Accepted:    446.5K
# Total Submissions: 861.5K
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
# 
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
# 
# 
# Example 1:
# 
# 
# Input: num1 = "11", num2 = "123"
# Output: "134"
# 
# 
# Example 2:
# 
# 
# Input: num1 = "456", num2 = "77"
# Output: "533"
# 
# 
# Example 3:
# 
# 
# Input: num1 = "0", num2 = "0"
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = deque()
        
        while i >= 0 and j >= 0:
            digit_i = ord(num1[i]) - ord('0')
            digit_j = ord(num2[j]) - ord('0')
            addition = digit_i + digit_j + carry
            if addition > 9:
                carry = 1
                addition %= 10
            else:
                carry = 0
            total = str(addition)
            result.appendleft(total)
            i -= 1
            j -= 1
        
        while i >= 0:
            digit_i = ord(num1[i]) - ord('0')
            addition = digit_i + carry
            if addition > 9:
                carry = 1
                addition %= 10
            else:
                carry = 0
            total = str(addition)
            result.appendleft(total)
            i -= 1

        while j >= 0:
            digit_j = ord(num2[j]) - ord('0')
            addition = digit_j + carry
            if addition > 9:
                carry = 1
                addition %= 10
            else:
                carry = 0
            total = str(addition)
            result.appendleft(total)
            j -= 1
        
        if carry:
            result.appendleft("1")

        return ''.join(list(result))
# "123"\n"456"\n
# "11"\n"123"\n
# "123"\n"45"\n
# "1"\n"9"\n
# @lc code=end
