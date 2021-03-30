#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Medium (45.46%)
# Likes:    1561
# Dislikes: 57
# Total Accepted:    190.5K
# Total Submissions: 417.2K
# Testcase Example:  '"eceba"\n2'
#
# Given a string s and an integer k, return the length of the longest substring
# of s that contains at most k distinct characters.
#
#
# Example 1:
#
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
#
# Example 2:
#
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ws, max_len, wl = 0, 0, {}

        for we in range(len(s)):
            if s[we] in wl:
                wl[s[we]] += 1
            else:
                wl[s[we]] = 1
            while len(wl) > k:
                if wl[s[ws]] == 1:
                    del wl[s[ws]]
                else:
                    wl[s[ws]] -= 1
                ws += 1
            max_len = max(max_len, we - ws + 1)

        return max_len


# @lc code=end
