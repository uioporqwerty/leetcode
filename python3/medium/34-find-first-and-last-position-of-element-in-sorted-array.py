#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (37.27%)
# Likes:    5144
# Dislikes: 196
# Total Accepted:    665.3K
# Total Submissions: 1.8M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
#
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index, end_index = -1, -1
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] == target:
                start_index = mid
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        if start_index == -1:
            return [start_index, end_index]

        i, j = start_index, len(nums) - 1
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] == target:
                end_index = mid
                i = mid + 1
            else:
                j = mid - 1

        return [start_index, end_index]


# @lc code=end
