#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
#
# algorithms
# Easy (82.11%)
# Likes:    186
# Dislikes: 8
# Total Accepted:    23.5K
# Total Submissions: 28.7K
# Testcase Example:  '["abc","car","ada","racecar","cool"]'
#
# Given an array of strings words, return the first palindromic string in the
# array. If there is no such string, return an empty string "".
# 
# A string is palindromic if it reads the same forward and backward.
# 
# 
# Example 1:
# 
# 
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# 
# 
# Example 2:
# 
# 
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# 
# 
# Example 3:
# 
# 
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is
# returned.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, word: str) -> bool:
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            palindrome = self.isPalindrome(word)
            if palindrome:
                return word
        
        return ""
# @lc code=end
