#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#
# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
#
# algorithms
# Easy (64.39%)
# Likes:    714
# Dislikes: 117
# Total Accepted:    81.4K
# Total Submissions: 125.7K
# Testcase Example:  '"this apple is sweet"\n"this apple is sour"'
#
# A sentence is a string of single-space separated words where each word
# consists only of lowercase letters.
# 
# A word is uncommon if it appears exactly once in one of the sentences, and
# does not appear in the other sentence.
# 
# Given two sentences s1 and s2, return a list of all the uncommon words. You
# may return the answer in any order.
# 
# 
# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_s1 = s1.split()
        words_s2 = s2.split() 

        word_count_s1 = Counter(words_s1)     
        word_count_s2 = Counter(words_s2)

        combined_word_count = word_count_s1 + word_count_s2

        uncommon_words = []

        for word in combined_word_count:
            if combined_word_count[word] == 1:
                uncommon_words.append(word)
        
        return uncommon_words
# @lc code=end
