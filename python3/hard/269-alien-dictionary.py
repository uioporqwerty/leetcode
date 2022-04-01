#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (34.51%)
# Likes:    3451
# Dislikes: 706
# Total Accepted:    279.2K
# Total Submissions: 803K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language that uses the English alphabet. However, the
# order among the letters is unknown to you.
# 
# You are given a list of strings words from the alien language's dictionary,
# where the strings in words are sorted lexicographically by the rules of this
# new language.
# 
# Return a string of the unique letters in the new alien language sorted in
# lexicographically increasing order by the new language's rules. If there is
# no solution, return "". If there are multiple solutions, return any of them.
# 
# A string s is lexicographically smaller than a string t if at the first
# letter where they differ, the letter in s comes before the letter in t in the
# alien language. If the first min(s.length, t.length) letters are the same,
# then s is smaller if and only if s.length < t.length.
# 
# 
# Example 1:
# 
# 
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# 
# 
# Example 2:
# 
# 
# Input: words = ["z","x"]
# Output: "zx"
# 
# 
# Example 3:
# 
# 
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""

        graph = {}
        indegrees = {}

        for word in words:
            for character in word:
                graph[character] = []
                indegrees[character] = 0

        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(0, min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                if parent != child:
                    graph[parent].append(child)
                    indegrees[child] += 1
                    break
            else:
                if len(w2) < len(w1):
                    return ""
                    
        sources = deque()
        for vertex in indegrees:
            if not indegrees[vertex]:
                sources.append(vertex)

        sorted_order = []
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)

            for child in graph[vertex]:
                indegrees[child] -= 1
                if not indegrees[child]:
                    sources.append(child)
        
        if len(sorted_order) != len(indegrees):
            return ""
        
        return "".join(sorted_order)
     
# @lc code=end
