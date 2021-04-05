#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (68.91%)
# Likes:    3440
# Dislikes: 182
# Total Accepted:    264.6K
# Total Submissions: 383.1K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
#
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        duplicates = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates


# @lc code=end
