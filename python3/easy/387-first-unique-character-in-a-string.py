#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (53.76%)
# Likes:    2697
# Dislikes: 133
# Total Accepted:    690.2K
# Total Submissions: 1.3M
# Testcase Example:  '"leetcode"'
#
# Given a string, find the first non-repeating character in it and return its
# index. If it doesn't exist, return -1.
#
# Examples:
#
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
#
#
# Note: You may assume the string contains only lowercase English letters.
#
#

# @lc code=start
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequencies = Counter(s)
        for i in range(len(s)):
            if frequencies[s[i]] == 1:
                return i
        return -1


# @lc code=end
