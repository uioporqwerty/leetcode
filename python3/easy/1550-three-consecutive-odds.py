#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#
# https://leetcode.com/problems/three-consecutive-odds/description/
#
# algorithms
# Easy (64.88%)
# Likes:    190
# Dislikes: 33
# Total Accepted:    31.7K
# Total Submissions: 49K
# Testcase Example:  '[2,6,4,1]'
#
# Given an integer array arr, return true if there are three consecutive odd
# numbers in the array. Otherwise, return false.
#
# Example 1:
#
#
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
#
#
# Example 2:
#
#
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
#
#
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        window_start = 0
        for window_end in range(len(arr)):
            while (window_end - window_start) > 3:
                window_start += 1
            if (
                (window_end - window_start + 1) >= 3
                and arr[window_end] % 2 != 0
                and arr[window_end - 1] % 2 != 0
                and arr[window_end - 2] % 2 != 0
            ):
                return True

        return False


# @lc code=end
