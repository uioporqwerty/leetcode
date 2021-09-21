#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
#
# https://leetcode.com/problems/second-largest-digit-in-a-string/description/
#
# algorithms
# Easy (47.90%)
# Likes:    131
# Dislikes: 52
# Total Accepted:    15.8K
# Total Submissions: 32.7K
# Testcase Example:  '"dfa12321afd"'
#
# Given an alphanumeric string s, return the second largest numerical digit
# that appears in s, or -1 if it does not exist.
# 
# An alphanumeric string is a string consisting of lowercase English letters
# and digits.
# 
# 
# Example 1:
# 
# 
# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest
# digit is 2.
# 
# 
# Example 2:
# 
# 
# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest
# digit. 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.
# 
# 
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        largest_digit = -1
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                largest_digit = max(largest_digit, ord(c) - ord('0'))
        
        second_largest_digit = -1
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                digit = ord(c) - ord('0')
                if digit != largest_digit and digit > second_largest_digit:
                    second_largest_digit = digit
        
        return second_largest_digit

# @lc code=end
