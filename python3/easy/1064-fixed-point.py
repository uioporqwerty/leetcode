#
# @lc app=leetcode id=1064 lang=python3
#
# [1064] Fixed Point
#
# https://leetcode.com/problems/fixed-point/description/
#
# algorithms
# Easy (64.30%)
# Likes:    226
# Dislikes: 52
# Total Accepted:    25.7K
# Total Submissions: 40.2K
# Testcase Example:  '[-10,-5,0,3,7]'
#
# Given an array of distinct integers arr, where arr is sorted in ascending
# order, return the smallest index i that satisfies arr[i] == i. If there is no
# such index, return -1.
# 
# 
# Example 1:
# 
# 
# Input: arr = [-10,-5,0,3,7]
# Output: 3
# Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0,
# arr[3] = 3, thus the output is 3.
# 
# Example 2:
# 
# 
# Input: arr = [0,2,5,8,17]
# Output: 0
# Explanation: arr[0] = 0, thus the output is 0.
# 
# Example 3:
# 
# 
# Input: arr = [-10,-5,3,4,7,9]
# Output: -1
# Explanation: There is no such i that arr[i] == i, thus the output is -1.
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length < 10^4
# -10^9 <= arr[i] <= 10^9
# 
# 
# 
# Follow up: The O(n) solution is very straightforward. Can we do better?
#

# @lc code=start
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        i, j = 0, len(arr) - 1
        min_index = float("inf")
    
        while i <= j:
            mid = (i + j) // 2
            if (arr[mid] >= 0 and arr[mid] == mid):
                min_index = min(mid, min_index)
                j = mid - 1
            elif (arr[mid] < 0 or arr[mid] < mid):
                i = mid + 1
            else:
                j = mid - 1
        return min_index if min_index != float("inf") else -1
# @lc code=end  
