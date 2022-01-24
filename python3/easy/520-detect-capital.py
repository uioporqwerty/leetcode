#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (54.27%)
# Likes:    998
# Dislikes: 318
# Total Accepted:    210.9K
# Total Submissions: 388.5K
# Testcase Example:  '"USA"'
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# 
# 
# Given a string word, return true if the usage of capitals in it is right.
# 
# 
# Example 1:
# Input: word = "USA"
# Output: true
# Example 2:
# Input: word = "FlaG"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count_capital_letters = 0
        for c in word:
            if c.isupper():
                count_capital_letters += 1
        return count_capital_letters == len(word) or (count_capital_letters == 1 and word[0].isupper()) or count_capital_letters == 0
            
# @lc code=end
