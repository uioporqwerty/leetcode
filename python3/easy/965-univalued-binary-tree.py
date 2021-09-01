#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (68.04%)
# Likes:    965
# Dislikes: 54
# Total Accepted:    133.1K
# Total Submissions: 195.1K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is uni-valued if every node in the tree has the same value.
# 
# Given the root of a binary tree, return true if the given tree is uni-valued,
# or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,1,1,1,1,null,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [2,2,2,5,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, common_value):
            if not root:
                return True
            
            if root.val != common_value:
                return False

            left = dfs(root.left, common_value)
            right = dfs(root.right, common_value)
            return left and right
        if root:
            common_value = root.val
            return dfs(root, common_value)
        else:
            return False
# @lc code=end
