#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (68.12%)
# Likes:    1865
# Dislikes: 272
# Total Accepted:    164.6K
# Total Submissions: 239.5K
# Testcase Example:  '"cba"\n"abcd"'
#
# You are given two strings order and s. All the words of order are unique and
# were sorted in some custom order previously.
# 
# Permute the characters of s so that they match the order that order was
# sorted. More specifically, if a character x occurs before a character y in
# order, then x should occur before y in the permuted string.
# 
# Return any permutation of s that satisfies this property.
# 
# 
# Example 1:
# 
# 
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c",
# "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned
# string. "dcba", "cdba", "cbda" are also valid outputs.
# 
# 
# Example 2:
# 
# 
# Input: order = "cbafg", s = "abcd"
# Output: "cbad"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.
# 
# 
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        indexes = {}
        order_indexes = set(order)
        ordered = []

        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = [i]
            else:
                indexes[s[i]].append(i)
        
        for i in range(len(order)):
            if order[i] not in indexes:
                continue
            s_indexes = indexes[order[i]]
            for j in range(len(s_indexes)):
                ordered.append(s[s_indexes[j]])
        
        for i in range(len(s)):
            if s[i] not in order_indexes:
                ordered.append(s[i])

        return ''.join(ordered) 
# "cba"\n"abcdc"\n
# "cbafg"\n"abcd"\n
# "exv"\n"xwvee"\n
# @lc code=end
