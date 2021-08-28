#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/
#
# algorithms
# Easy (64.86%)
# Likes:    386
# Dislikes: 16
# Total Accepted:    41.1K
# Total Submissions: 63.7K
# Testcase Example:  '"i love eating burger"\n"burg"'
#
# Given a sentence that consists of some words separated by a single space, and
# a searchWord, check if searchWord is a prefix of any word in sentence.
# 
# Return the index of the word in sentence (1-indexed) where searchWord is a
# prefix of this word. If searchWord is a prefix of more than one word, return
# the index of the first word (minimum index). If there is no such word return
# -1.
# 
# A prefix of a string s is any leading contiguous substring of s.
# 
# 
# Example 1:
# 
# 
# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the
# sentence.
# 
# 
# Example 2:
# 
# 
# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word
# in the sentence, but we return 2 as it's the minimal index.
# 
# 
# Example 3:
# 
# 
# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.
# 
# 
# Example 4:
# 
# 
# Input: sentence = "i use triple pillow", searchWord = "pill"
# Output: 4
# 
# 
# Example 5:
# 
# 
# Input: sentence = "hello from the other side", searchWord = "they"
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= sentence.length <= 100
# 1 <= searchWord.length <= 10
# sentence consists of lowercase English letters and spaces.
# searchWord consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i in range(len(words)):
            k = 0
            j = 0
            while j < len(words[i]):
                while j < len(words[i]) and k < len(searchWord) and words[i][j] == searchWord[k]:
                    j += 1
                    k += 1

                if k >= len(searchWord):
                    return i + 1
                
                if j >= len(words[i]) or words[i][j] != searchWord[k]:
                    break

        return -1
# @lc code=end
