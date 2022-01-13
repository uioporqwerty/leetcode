#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (55.96%)
# Likes:    2111
# Dislikes: 252
# Total Accepted:    464.8K
# Total Submissions: 829.7K
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
# 
# 
# Constraints:
# 
# 
# 0 <= rowIndex <= 33
# 
# 
# 
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = [1,1]

        for i in range(3, rowIndex + 2):
            row = [1] * i
            for j in range(1, len(row) - 1):
                row[j] = prev_row[j - 1] + prev_row[j]
            prev_row = list(row)

        return prev_row
# @lc code=end
