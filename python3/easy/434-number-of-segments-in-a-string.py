#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (37.78%)
# Likes:    291
# Dislikes: 850
# Total Accepted:    91.2K
# Total Submissions: 241.6K
# Testcase Example:  '"Hello, my name is John"'
#
# You are given a string s, return the number of segments in the string.
#
# A segment is defined to be a contiguous sequence of non-space characters.
#
#
# Example 1:
#
#
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
#
#
# Example 2:
#
#
# Input: s = "Hello"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "love live! mu'sic forever"
# Output: 4
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
# 0 <= s.length <= 300
# s consists of lower-case and upper-case English letters, digits or one of the
# following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.
#
#
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        num_segments = 0
        i = 0
        # Skip spaces beginning of string
        while i < len(s) and s[i] == " ":
            i += 1

        while i < len(s):
            # Skip characters until first space or end of string encountered
            while i < len(s) and s[i] != " ":
                i += 1

            num_segments += 1

            # Skip spaces after segment
            while i < len(s) and s[i] == " ":
                i += 1

        return num_segments


# @lc code=end
