#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#
# https://leetcode.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (63.21%)
# Likes:    688
# Dislikes: 63
# Total Accepted:    137K
# Total Submissions: 215.2K
# Testcase Example:  '"code"'
#
# Given a string s, return true if a permutation of the string could form a
# palindrome.
# 
# 
# Example 1:
# 
# 
# Input: s = "code"
# Output: false
# 
# 
# Example 2:
# 
# 
# Input: s = "aab"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "carerac"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5000
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = [0] * 26
        odd_char_count = 0
        for char in s:
            counts[ord(char) - ord('a')] += 1
        for count in counts:
            if count % 2 != 0:
                odd_char_count += 1
        return odd_char_count <= 1
# @lc code=end
