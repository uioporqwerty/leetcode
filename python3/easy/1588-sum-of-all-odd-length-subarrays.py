#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
#
# algorithms
# Easy (81.74%)
# Likes:    1126
# Dislikes: 113
# Total Accepted:    59.9K
# Total Submissions: 72.9K
# Testcase Example:  '[1,4,2,5,3]'
#
# Given an array of positive integers arr, calculate the sum of all possible
# odd-length subarrays.
# 
# A subarray is a contiguous subsequence of the array.
# 
# Return the sum of all odd-length subarrays of arr.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 =
# 58
# 
# Example 2:
# 
# 
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum
# is 3.
# 
# Example 3:
# 
# 
# Input: arr = [10,11,12]
# Output: 66
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sums = {0:0}
        current_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            prefix_sums[i] = current_sum
        window_start = 0
        window_end = 2
        multiple = 3
        total_sum = sum(arr)
        while window_end < len(arr):
            current_sum = prefix_sums[window_end] - prefix_sums[window_start - 1] if window_start > 0 else prefix_sums[window_end]
            total_sum += current_sum
            window_end += 1
            window_start += 1
            if window_end >= len(arr):
                window_start = 0
                multiple += 2
                window_end = multiple - 1
                
        
        return total_sum
            
# @lc code=end
