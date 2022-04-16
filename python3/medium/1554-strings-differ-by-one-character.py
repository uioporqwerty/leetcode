#
# @lc app=leetcode id=1554 lang=python3
#
# [1554] Strings Differ by One Character
#
# https://leetcode.com/problems/strings-differ-by-one-character/description/
#
# algorithms
# Medium (65.63%)
# Likes:    230
# Dislikes: 11
# Total Accepted:    12.9K
# Total Submissions: 21.6K
# Testcase Example:  '["abcd","acbd", "aacd"]'
#
# Given a list of strings dict where all the strings are of the same length.
# 
# Return true if there are 2 strings that only differ by 1 character in the
# same index, otherwise return false.
# 
# 
# Example 1:
# 
# 
# Input: dict = ["abcd","acbd", "aacd"]
# Output: true
# Explanation: Strings "abcd" and "aacd" differ only by one character in the
# index 1.
# 
# 
# Example 2:
# 
# 
# Input: dict = ["ab","cd","yz"]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: dict = ["abcd","cccc","abyd","abab"]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of characters in dict <= 10^5
# dict[i].length == dict[j].length
# dict[i] should be unique.
# dict[i] contains only lowercase English letters.
# 
# 
# 
# Follow up: Could you solve this problem in O(n * m) where n is the length of
# dict and m is the length of each string.
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):
            patterns = set()
            for word in dict:
                myWord = word[:i] + word[i+1:]
                if myWord in patterns:
                    return True
                patterns.add(myWord)                            
                
        return False
                    
# @lc code=end
