#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (50.41%)
# Likes:    10937
# Dislikes: 336
# Total Accepted:    1.5M
# Total Submissions: 2.9M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-Up
        # O(n) time
        # O(n) space
        
        if n <= 2:
            return n

        A = [0] * (n + 1)
        A[1] = 1
        A[2] = 2

        for i in range(3, n + 1):
            A[i] = A[i - 1] + A[i - 2]
        
        return A[n]
        # Top Down
        # O(n) time
        # O(n) space
        # memo = {}
        # def dp(n):
        #     if n <= 2:
        #         return n
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = dp(n - 1) + dp(n - 2)
        #     return memo[n]
        
        # return dp(n)
# @lc code=end
