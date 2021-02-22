#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (58.57%)
# Likes:    2339
# Dislikes: 158
# Total Accepted:    758.9K
# Total Submissions: 1.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
#

# @lc code=start
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution 1: Sorted Array
        O(nlogn + nlogn) time
        O(s + t) space
        if len(s) != len(t):
            return False

        s_arr = sorted(list(s))
        t_arr = sorted(list(t))

        for i in range(len(s_arr)):
            if s_arr[i] != t_arr[i]:
                return False

        return True
        """

        """
        Instance counting with Counter class. Also doable with dictionaries and arrays if dealing with ascii only.
        O(nlogn _ nlogn) time
        O(s + t) space
        """
        s_freq, t_freq = Counter(s), Counter(t)

        return s_freq == t_freq


# @lc code=end
