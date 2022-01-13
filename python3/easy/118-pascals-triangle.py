#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (61.90%)
# Likes:    4515
# Dislikes: 186
# Total Accepted:    677.1K
# Total Submissions: 1.1M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= numRows <= 30
# 
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[1], [1,1]]
        if numRows == 2:
            return dp
        
        for i in range(3, numRows + 1):
            row = [1] * i
            for j in range(1, len(row) - 1):
                row[j] = dp[i-2][j - 1] + dp[i-2][j]
            dp.append(row)
        return dp
# @lc code=end
