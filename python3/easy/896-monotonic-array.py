#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (58.01%)
# Likes:    923
# Dislikes: 43
# Total Accepted:    144.4K
# Total Submissions: 249K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
# A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: [1,2,2,3]
# Output: true
#
#
#
# Example 2:
#
#
# Input: [6,5,4,4]
# Output: true
#
#
#
# Example 3:
#
#
# Input: [1,3,2]
# Output: false
#
#
#
# Example 4:
#
#
# Input: [1,2,4,5]
# Output: true
#
#
#
# Example 5:
#
#
# Input: [1,1,1]
# Output: true
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
#
#
#
#
#
#
#
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A:
            return True

        is_increasing = A[0] <= A[-1]
        for i in range(1, len(A)):
            if (is_increasing and A[i - 1] > A[i]) or (
                not is_increasing and A[i - 1] < A[i]
            ):
                return False

        return True


# @lc code=end
