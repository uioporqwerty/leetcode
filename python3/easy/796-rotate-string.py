#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.25%)
# Likes:    1027
# Dislikes: 59
# Total Accepted:    93.9K
# Total Submissions: 191.1K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
#
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
#
# Note:
#
#
# A and B will have length at most 100.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        q = deque(list(A))
        for i in range(len(q)):
            if "".join(q) == B:
                return True
            letter = q.popleft()
            q.append(letter)

        return False


# @lc code=end
