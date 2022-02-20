#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#
# https://leetcode.com/problems/minimize-deviation-in-array/description/
#
# algorithms
# Hard (48.38%)
# Likes:    1264
# Dislikes: 62
# Total Accepted:    32.3K
# Total Submissions: 63K
# Testcase Example:  '[1,2,3,4]'
#
# You are given an array nums of n positive integers.
# 
# You can perform two types of operations on any element of the array any
# number of times:
# 
# 
# If the element is even, divide it by 2.
# 
# 
# For example, if the array is [1,2,3,4], then you can do this operation on the
# last element, and the array will be [1,2,3,2].
# 
# 
# If the element is odd, multiply it by 2.
# 
# For example, if the array is [1,2,3,4], then you can do this operation on the
# first element, and the array will be [2,2,3,4].
# 
# 
# 
# 
# The deviation of the array is the maximum difference between any two elements
# in the array.
# 
# Return the minimum deviation the array can have after performing some number
# of operations.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
# then the deviation will be 3 - 2 = 1.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3],
# then the deviation will be 5 - 2 = 3.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,10,8]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 2 <= n <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
from heapq import *

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        minimum = float("inf")
        
        for num in nums:
            if num % 2 == 0:
                minimum = min(minimum, num)
                evens.append(-num)
            else:
                minimum = min(minimum, num * 2)
                evens.append(-num * 2)

        heapify(evens)

        deviation = float("inf")

        while evens:
            max_element = -1 * heappop(evens)
            deviation = min(deviation, max_element - minimum)
            
            if max_element % 2 == 0:
                minimum = min(minimum, max_element // 2)
                heappush(evens, -max_element // 2)
            else:
                break

        return deviation
        
# @lc code=end
