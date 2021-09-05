#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.64%)
# Likes:    1008
# Dislikes: 252
# Total Accepted:    278.7K
# Total Submissions: 517K
# Testcase Example:  '"a"\n"b"'
#
# Given two stings ransomNote and magazine, return true if ransomNote can be
# constructed from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts_ransom = Counter(ransomNote)
        for letter in magazine:
            if letter in counts_ransom:
                counts_ransom[letter] -= 1
        for count in counts_ransom:
            if counts_ransom[count] > 0:
                return False
        
        return True
# @lc code=end
