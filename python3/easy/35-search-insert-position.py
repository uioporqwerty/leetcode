#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.86%)
# Likes:    4284
# Dislikes: 312
# Total Accepted:    913.7K
# Total Submissions: 2.1M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:
# Input: nums = [1], target = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        i, j = 0, len(nums) - 1
        insertion_index = -1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                insertion_index = mid + 1
                i = mid + 1
        
        return insertion_index
# @lc code=end
