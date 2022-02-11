#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.20%)
# Likes:    4480
# Dislikes: 126
# Total Accepted:    300.1K
# Total Submissions: 678K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = Counter(s1)
        
        i = 0
        counts_s2 = Counter()
        
        for j in range(len(s2)):
            if (j - i) >= len(s1):
                if counts_s2[s2[i]] == 1:
                    del counts_s2[s2[i]]
                else:
                    counts_s2[s2[i]] -= 1
                    
                i += 1
                
            counts_s2[s2[j]] = 1 + counts_s2[s2[j]] if s2[j] in counts_s2 else 1
            
            if counts_s1 == counts_s2:
                return True
        
        return False
        
# @lc code=end
