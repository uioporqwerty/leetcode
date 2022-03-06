#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (71.14%)
# Likes:    2914
# Dislikes: 147
# Total Accepted:    261.5K
# Total Submissions: 368.4K
# Testcase Example:  '"abbaca"'
#
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing
# them.
# 
# We repeatedly make duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It
# can be proven that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
# 
# 
# Example 2:
# 
# 
# Input: s = "azxxzy"
# Output: "ay"
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
    def removeDuplicates(self, s: str) -> str:
        # O(n) time O(n - d) space
        stack = []

        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(stack)
        
# @lc code=end
