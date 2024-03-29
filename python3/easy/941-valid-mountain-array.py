#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (32.34%)
# Likes:    1461
# Dislikes: 123
# Total Accepted:    231.5K
# Total Submissions: 708.3K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i, j = 0, len(arr) - 1
        while i < len(arr):
            if i + 1 < len(arr) and arr[i + 1] > arr[i]:
                i += 1
            else:
                break
        
        if i >= len(arr) - 1:
            return False

        while j > 0:
            if j - 1 > 0 and arr[j - 1] > arr[j]:
                j -= 1
            else:
                break
        
        if j <= 0:
            return False

        return i == j
# @lc code=end
