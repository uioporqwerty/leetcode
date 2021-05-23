#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
#
# algorithms
# Easy (83.57%)
# Likes:    174
# Dislikes: 4
# Total Accepted:    27K
# Total Submissions: 32.3K
# Testcase Example:  '"thequickbrownfoxjumpsoverthelazydog"'
#
# A pangram is a sentence where every letter of the English alphabet appears at
# least once.
# 
# Given a string sentence containing only lowercase English letters, return
# true if sentence is a pangram, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English
# alphabet.
# 
# 
# Example 2:
# 
# 
# Input: sentence = "leetcode"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [0] * 26
        alphabet_seen = 26
        for c in sentence:
            if alphabet[ord(c) - ord('a')] == 0:
                alphabet_seen -= 1
            alphabet[ord(c) - ord('a')] += 1
        
        return alphabet_seen == 0

# @lc code=end

