#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (58.78%)
# Likes:    2878
# Dislikes: 254
# Total Accepted:    466.5K
# Total Submissions: 778K
# Testcase Example:  '"A"'
#
# Given a string columnTitle that represents the column title as appear in an
# Excel sheet, return its corresponding column number.
# 
# For example:
# 
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 
# 
# 
# Example 1:
# 
# 
# Input: columnTitle = "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: columnTitle = "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: columnTitle = "ZY"
# Output: 701
# 
# 
# 
# Constraints:
# 
# 
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
# 
# 
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[i]) - ord('A') + 1
        
        return result
# @lc code=end
