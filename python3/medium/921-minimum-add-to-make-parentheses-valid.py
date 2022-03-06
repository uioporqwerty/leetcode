#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (77.49%)
# Likes:    2264
# Dislikes: 130
# Total Accepted:    186.4K
# Total Submissions: 241.2K
# Testcase Example:  '"())"'
#
# A parentheses string is valid if and only if:
# 
# 
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# You are given a parentheses string s. In one move, you can insert a
# parenthesis at any position of the string.
# 
# 
# For example, if s = "()))", you can insert an opening parenthesis to be
# "(()))" or a closing parenthesis to be "())))".
# 
# 
# Return the minimum number of moves required to make s valid.
# 
# 
# Example 1:
# 
# 
# Input: s = "())"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: s = "((("
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
# 
# 
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # O(n) time O(1) space
        answer = balance = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance == -1:
                answer += 1
                balance += 1
        
        return answer + balance

        # O(n) time O(n) space
        # stack =[]

        # for i in range(len(s)):
        #     if stack and s[i] == ')' and stack[-1] == '(':
        #         stack.pop()
        #     else:
        #         stack.append(s[i])
            
        # return len(stack)
# @lc code=end
