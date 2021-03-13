#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (56.62%)
# Likes:    1465
# Dislikes: 830
# Total Accepted:    741.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(nlogn) Time
        # O(1) Space
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         return True

        # return False

        # O(n) Time
        # O(n) Space
        unique_elements = set(nums)
        return len(nums) != len(unique_elements)


# @lc code=end
