#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#
# https://leetcode.com/problems/valid-word-abbreviation/description/
#
# algorithms
# Easy (33.55%)
# Likes:    437
# Dislikes: 1597
# Total Accepted:    92.9K
# Total Submissions: 268.1K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
# A string can be abbreviated by replacing any number of non-adjacent,
# non-empty substrings with their lengths. The lengths should not have leading
# zeros.
# 
# For example, a string such as "substitution" could be abbreviated as (but not
# limited to):
# 
# 
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# 
# 
# The following are not valid abbreviations:
# 
# 
# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# 
# 
# Given a string word and an abbreviation abbr, return whether the string
# matches the given abbreviation.
# 
# A substring is a contiguous non-empty sequence of characters within a
# string.
# 
# 
# Example 1:
# 
# 
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n"
# ("i nternational iz atio n").
# 
# 
# Example 2:
# 
# 
# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 20
# word consists of only lowercase English letters.
# 1 <= abbr.length <= 10
# abbr consists of lowercase English letters and digits.
# All the integers in abbr will fit in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(abbr):
            char = abbr[i]
            if j >= len(word) or char == "0" or (not char.isdigit() and word[j] != char):
                return False

            if char.isdigit():
                num_start = i
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                num = int(abbr[num_start:i])
                if num > len(word) - j:
                    return False
                while j < len(word) and num > 0:
                    j += 1
                    num -= 1
            else:
                j += 1
                i += 1
                
        return i >= len(abbr) and j >= len(word)

# @lc code=end
