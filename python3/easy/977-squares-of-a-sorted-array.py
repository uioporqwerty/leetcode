#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (72.08%)
# Likes:    2137
# Dislikes: 114
# Total Accepted:    436.2K
# Total Submissions: 606.3K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
#
#
# Example 1:
#
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
#
# Example 2:
#
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
#
#
#
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] * len(nums)
        i, j, k = 0, len(nums) - 1, len(nums) - 1

        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                squares[k] = nums[i] ** 2
                i += 1
            else:
                squares[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return squares


# @lc code=end
