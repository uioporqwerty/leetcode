#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (38.25%)
# Likes:    4223
# Dislikes: 253
# Total Accepted:    422.5K
# Total Submissions: 1.1M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                isValid1 = self.isPalindrome(s, i, j - 1)
                isValid2 = self.isPalindrome(s, i + 1, j)
                if isValid1 or isValid2:
                    return True
                else:
                    return False
            i += 1
            j -= 1
        
        return True
# "aa"\n
# "a"\n
# "ab"\n
# "abcca"\n
# "abccdedfa"\n
# "cbbcc"\n
# @lc code=end
