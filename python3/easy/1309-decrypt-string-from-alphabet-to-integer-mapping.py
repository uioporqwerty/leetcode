#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
#
# algorithms
# Easy (77.81%)
# Likes:    653
# Dislikes: 61
# Total Accepted:    61.9K
# Total Submissions: 79.5K
# Testcase Example:  '"10#11#12"'
#
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to
# English lowercase characters as follows:
#
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#
#
# Return the string formed after mapping.
#
# It's guaranteed that a unique mapping will always exist.
#
#
# Example 1:
#
#
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#
#
# Example 2:
#
#
# Input: s = "1326#"
# Output: "acz"
#
#
# Example 3:
#
#
# Input: s = "25#"
# Output: "y"
#
#
# Example 4:
#
#
# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s[i] only contains digits letters ('0'-'9') and '#' letter.
# s will be valid string such that mapping is always possible.
#
#
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        res = []
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                res.append(chr(int(s[i] + s[i + 1]) - 1 + ord("a")))
                i += 3
            else:
                res.append(chr((ord(s[i]) - ord("1")) + ord("a")))
                i += 1

        return "".join(res)


# @lc code=end
