#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (65.18%)
# Likes:    3619
# Dislikes: 69
# Total Accepted:    349.5K
# Total Submissions: 535.7K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters.
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# 
# 
# Example 3:
# 
# 
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either'(' , ')', or lowercase English letter.
# 
# 
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(N) time O(N) space
        result = []
        p_stack = []


        for i in range(len(s)):
            if s[i] == ')':
                if p_stack and p_stack[-1][0] == '(':
                    p_stack.pop()
                    result.append(s[i])
                else:
                    result.append(None)
            else:
                if s[i] == '(':
                    p_stack.append(('(', i))
                result.append(s[i])

        while p_stack:
            _, index = p_stack.pop()
            result[index] = None
        
        return ''.join([x for x in result if x is not None])
# @lc code=end
