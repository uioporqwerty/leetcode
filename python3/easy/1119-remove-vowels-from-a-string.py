#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#
# https://leetcode.com/problems/remove-vowels-from-a-string/description/
#
# algorithms
# Easy (90.50%)
# Likes:    169
# Dislikes: 89
# Total Accepted:    62.1K
# Total Submissions: 68.6K
# Testcase Example:  '"leetcodeisacommunityforcoders"'
#
# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and
# return the new string.
#
#
# Example 1:
#
#
# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
#
#
# Example 2:
#
#
# Input: s = "aeiou"
# Output: ""
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of only lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def removeVowels(self, s: str) -> str:
        result = []
        vowels = set(["a", "e", "i", "o", "u"])

        for c in s:
            if c not in vowels:
                result.append(c)

        return "".join(result)


# @lc code=end
