#
# @lc app=leetcode id=1570 lang=python3
#
# [1570] Dot Product of Two Sparse Vectors
#
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
#
# algorithms
# Medium (90.59%)
# Likes:    607
# Dislikes: 79
# Total Accepted:    107.8K
# Total Submissions: 119K
# Testcase Example:  '[1,0,0,2,3]\n[0,3,0,4,0]'
#
# Given two sparse vectors, compute their dot product.
# 
# Implement class SparseVector:
# 
# 
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector
# and vec
# 
# 
# A sparse vector is a vector that has mostly zero values, you should store the
# sparse vector efficiently and compute the dot product between two
# SparseVector.
# 
# Follow up: What if only one of the vectors is sparse?
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start
class SparseVector:
    def __init__(self, nums: List[int]):
        self.internal_nums = []
        for i in range(len(nums)):
            if nums[i] != 0:
                self.internal_nums.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i, j = 0, 0
        product = None
        
        while i < len(self.internal_nums) and j < len(vec.internal_nums):
            if self.internal_nums[i][0] < vec.internal_nums[j][0]:
                i += 1
            elif self.internal_nums[i][0] > vec.internal_nums[j][0]:
                j += 1
            else:
                product = self.internal_nums[i][1] * vec.internal_nums[j][1] if not product else product + self.internal_nums[i][1] * vec.internal_nums[j][1] 
                i += 1
                j += 1
        
        return product if product else 0

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# @lc code=end
