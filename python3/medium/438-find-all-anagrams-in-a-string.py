# @before-stub-for-debug-begin
from python3problem438 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (47.01%)
# Likes:    6583
# Dislikes: 242
# Total Accepted:    474.4K
# Total Submissions: 995.8K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# 
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_freq = Counter(p)
        s_freq = Counter()
        
        for i in range(len(s)):
            s_freq[s[i]] += 1

            if i >= len(p):
                if s_freq[s[i - len(p)]] == 1:
                    del s_freq[s[i - len(p)]]
                else:
                    s_freq[s[i - len(p)]] -= 1
            
            if s_freq == p_freq:
                result.append(i - len(p) + 1)

        return result
        # "abab"\n"ab"\n
# @lc code=end
