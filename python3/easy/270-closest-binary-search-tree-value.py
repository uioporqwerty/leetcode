#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (52.88%)
# Likes:    1302
# Dislikes: 84
# Total Accepted:    232.5K
# Total Submissions: 439.1K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given the root of a binary search tree and a target value, return the value
# in the BST that is closest to the target.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: root = [1], target = 4.428571
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        distance_to_value = float("inf")
        min_val = -1
        def dfs(root: TreeNode):
            nonlocal distance_to_value
            nonlocal min_val
            if not root:
                return
            if abs(target - root.val) < distance_to_value:
                distance_to_value = abs(target - root.val)
                min_val = root.val
            if root.val > target:
                dfs(root.left)
            if root.val < target:
                dfs(root.right)
        
        dfs(root)
        return min_val
# @lc code=end
