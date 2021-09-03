#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (64.51%)
# Likes:    1360
# Dislikes: 52
# Total Accepted:    138.9K
# Total Submissions: 215K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +'[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree, from left to right order, the
# values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
# 
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root1 = [1], root2 = [1]
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: root1 = [1], root2 = [2]
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: root1 = [1,2], root2 = [2,2]
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, leaf_sequence: [int]):
          if root:
            if not root.left and not root.right:
              leaf_sequence.append(root.val)
            dfs(root.left, leaf_sequence)
            dfs(root.right, leaf_sequence)
        
        root_1_leaf_sequence = []
        root_2_leaf_sequence = []

        dfs(root1, root_1_leaf_sequence)
        dfs(root2, root_2_leaf_sequence)
        
        if len(root_1_leaf_sequence) != len(root_2_leaf_sequence):
          return False
        
        for i in range(len(root_1_leaf_sequence)):
          leaf_1 = root_1_leaf_sequence[i]
          leaf_2 = root_2_leaf_sequence[i]
          if leaf_1 != leaf_2:
            return False
          
        return True
# @lc code=end
