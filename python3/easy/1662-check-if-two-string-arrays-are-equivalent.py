#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
#
# algorithms
# Easy (83.13%)
# Likes:    315
# Dislikes: 76
# Total Accepted:    73K
# Total Submissions: 88.2K
# Testcase Example:  '["ab", "c"]\n["a", "bc"]'
#
# Given two string arrays word1 and word2, return true if the two arrays
# represent the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in
# order forms the string.
#
#
# Example 1:
#
#
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
#
# Example 2:
#
#
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
#
#
# Example 3:
#
#
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 10^3
# 1 <= word1[i].length, word2[i].length <= 10^3
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
# word1[i] and word2[i] consist of lowercase letters.
#
#
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Time: O(n)
        # Space: O(n)
        word_1 = "".join(word1)
        word_2 = "".join(word2)

        return word_1 == word_2


# @lc code=end
