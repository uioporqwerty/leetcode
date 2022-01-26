#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
#
# algorithms
# Easy (76.77%)
# Likes:    262
# Dislikes: 8
# Total Accepted:    27.2K
# Total Submissions: 35.3K
# Testcase Example:  '"abacbc"'
#
# Given a string s, return true if s is a good string, or false otherwise.
# 
# A string s is good if all the characters that appear in s have the same
# number of occurrences (i.e., the same frequency).
# 
# 
# Example 1:
# 
# 
# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All
# characters occur 2 times in s.
# 
# 
# Example 2:
# 
# 
# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of
# times.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:

    def areOccurrencesEqual(self, s: str) -> bool:
        word_count = [0] * 26

        for c in s:
            word_count[ord(c) - ord('a')] += 1

        initial_occurrence_count = 0
        for i in range(len(word_count)):
            if word_count[i] != 0 and initial_occurrence_count == 0:
                initial_occurrence_count = word_count[i]
            
            if word_count[i] != 0 and initial_occurrence_count != 0 and word_count[i] != initial_occurrence_count:
                return False

        return True
# @lc code=end
