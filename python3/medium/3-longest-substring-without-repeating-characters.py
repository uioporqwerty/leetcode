#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.40%)
# Likes:    13191
# Dislikes: 685
# Total Accepted:    2M
# Total Submissions: 6.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen_characters = set()
        window_start = 0
        for window_end in range(len(s)):
            while s[window_end] in seen_characters:
                seen_characters.remove(s[window_start])
                window_start += 1
            seen_characters.add(s[window_end])
            max_length = max(max_length, (window_end - window_start) + 1)

        return max_length


# @lc code=end
