#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (39.25%)
# Likes:    3126
# Dislikes: 360
# Total Accepted:    331.6K
# Total Submissions: 829.7K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
# 
# 
# Example 1:
# 
# 
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp_words = {}
        mp_letters = [''] * 26
        words = s.split()
        i = 0

        while i < len(pattern) and i < len(words):
            if (words[i] in mp_words and mp_words[words[i]] != pattern[i]) or (mp_letters[ord(pattern[i]) - ord('a')] != '' and mp_letters[ord(pattern[i]) - ord('a')] != words[i]):
                return False
            mp_words[words[i]] = pattern[i]
            mp_letters[ord(pattern[i]) - ord('a')] = words[i]
            i += 1
            
        return i > len(words) - 1 and i > len(pattern) - 1
        
# @lc code=end
