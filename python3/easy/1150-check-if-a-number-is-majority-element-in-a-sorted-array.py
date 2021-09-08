#
# @lc app=leetcode id=1150 lang=python3
#
# [1150] Check If a Number Is Majority Element in a Sorted Array
#
# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/description/
#
# algorithms
# Easy (57.01%)
# Likes:    232
# Dislikes: 28
# Total Accepted:    24.7K
# Total Submissions: 43.3K
# Testcase Example:  '[2,4,5,5,5,5,5,6,6]\n5'
#
# Given an integer array nums sorted in non-decreasing order and an integer
# target, return true if target is a majority element, or false otherwise.
# 
# A majority element in an array nums is an element that appears more than
# nums.length / 2 times in the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation: The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation: The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i], target <= 10^9
# nums is sorted in non-decreasing order.
# 
# 
#

# @lc code=start
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start = -1
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                start = mid
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        end = -1
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                end = mid
                i = mid + 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        if start == -1 or end == -1:
            return False
            
        appearence = end - start + 1
        return appearence > (len(nums) / 2)
# @lc code=end
