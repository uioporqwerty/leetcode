#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (72.94%)
# Likes:    1673
# Dislikes: 111
# Total Accepted:    283.1K
# Total Submissions: 383.3K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.
# 
# 
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def reverseWord(self, s: str) -> str:
        i, j = 0, len(s) - 1
        arr = list(s)
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return ''.join(arr)

    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = []
        for word in words:
            reversed_words.append(self.reverseWord(word))
        
        return ' '.join(reversed_words)
        
# @lc code=end
