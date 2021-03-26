#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (50.43%)
# Likes:    1239
# Dislikes: 21
# Total Accepted:    138.7K
# Total Submissions: 274.8K
# Testcase Example:  '"eceba"'
#
# Given a string s , find the length of the longest substring t  that contains
# at most 2 distinct characters.
#
# Example 1:
#
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
#
#
# Example 2:
#
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinct_set = {}
        window_start = 0
        max_length = 0
        for window_end in range(len(s)):
            if s[window_end] in distinct_set:
                distinct_set[s[window_end]] += 1
            else:
                distinct_set[s[window_end]] = 1
            while len(distinct_set) > 2:
                if distinct_set[s[window_start]] == 1:
                    del distinct_set[s[window_start]]
                else:
                    distinct_set[s[window_start]] -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)

        return max_length


# @lc code=end
