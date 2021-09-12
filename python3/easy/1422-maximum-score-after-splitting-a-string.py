#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
#
# algorithms
# Easy (57.64%)
# Likes:    402
# Dislikes: 21
# Total Accepted:    33.5K
# Total Submissions: 58K
# Testcase Example:  '"011101"'
#
# Given a string s of zeros and ones, return the maximum score after splitting
# the string into two non-empty substrings (i.e. left substring and right
# substring).
# 
# The score after splitting a string is the number of zeros in the left
# substring plus the number of ones in the right substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
# 
# 
# Example 2:
# 
# 
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2
# + 3 = 5
# 
# 
# Example 3:
# 
# 
# Input: s = "1111"
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.
# 
# 
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        if not s:
            return max_score
        left_score, right_score = 1 if s[0] == "0" else 0, 0
        for i in range(1, len(s)):
            if s[i] == "1":
                right_score += 1
        left = 0
        for right in range(1, len(s)):
            if right > 1:
                right_score -= 1 if int(s[left]) == 1 else 0
                left_score += 1 if int(s[left]) == 0 else 0
            max_score = max(max_score, left_score + right_score)
            left += 1
        
        return max_score
# @lc code=end
