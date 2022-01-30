#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (33.37%)
# Likes:    14214
# Dislikes: 1808
# Total Accepted:    1.2M
# Total Submissions: 3.6M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #O(min(A, B)) time O(1) space
        A, B = nums1, nums2

        if len(nums2) < len(nums1):
            A, B = nums2, nums1
        
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i + 1 < len(A) else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 < len(B)  else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right) 
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
    


        # O(m + n) time O(m + n) space
        # merged = []
        
        # i, j = 0, 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] <= nums2[j]:
        #         merged.append(nums1[i])
        #         i += 1
        #     else:
        #         merged.append(nums2[j])
        #         j += 1
        
        # while i < len(nums1):
        #     merged.append(nums1[i])
        #     i += 1
        
        # while j < len(nums2):
        #     merged.append(nums2[j])
        #     j += 1
        
        # if not merged:
        #     return 0
        
        # if len(merged) % 2 == 0:
        #     return (merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2.0
        
        # return merged[len(merged) // 2]
# @lc code=end
