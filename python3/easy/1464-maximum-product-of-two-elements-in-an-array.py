#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
#
# algorithms
# Easy (77.89%)
# Likes:    776
# Dislikes: 131
# Total Accepted:    115.6K
# Total Submissions: 148.3K
# Testcase Example:  '[3,4,5,2]'
#
# Given the array of integers nums, you will choose two different indices i and
# j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
# 
# Example 1:
# 
# 
# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will
# get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 =
# 12. 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get
# the maximum value of (5-1)*(5-1) = 16.
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,7]
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) time O(1) space
        first_max = float("-inf")
        second_max = float("-inf")

        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        return (first_max - 1) * (second_max - 1)
        # O(n^2) time O(1) space
        # max_product = float("-inf")

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         product = (nums[i] - 1) * (nums[j] - 1)
        #         max_product = max(max_product, product)
        
        # return max_product
# @lc code=end
