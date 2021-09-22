#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (46.64%)
# Likes:    716
# Dislikes: 124
# Total Accepted:    117.6K
# Total Submissions: 241K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# Given a character array s, reverse the order of the words.
# 
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by a single space.
# 
# Your code must solve the problem in-place, i.e. without allocating extra
# space.
# 
# 
# Example 1:
# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Example 2:
# Input: s = ["a"]
# Output: ["a"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
# There is at least one word in s.
# s does not contain leading or trailing spaces.
# All the words in s are guaranteed to be separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        i, j = 0, 0

        while j < len(s):
            while j < len(s) and s[j] != ' ':
                j += 1
            r_i, r_j = i, j - 1
            while r_i < r_j:
                s[r_i], s[r_j] = s[r_j], s[r_i]
                r_i += 1
                r_j -= 1
            j += 1
            i = j

        return s
        
# @lc code=end
