#
# @lc app=leetcode id=1644 lang=python3
#
# [1644] Lowest Common Ancestor of a Binary Tree II
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/
#
# algorithms
# Medium (56.77%)
# Likes:    233
# Dislikes: 9
# Total Accepted:    19.7K
# Total Submissions: 34.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given the root of a binary tree, return the lowest common ancestor (LCA) of
# two given nodes, p and q. If either node p or q does not exist in the tree,
# return null. All values of the nodes in the tree are unique.
# 
# According to the definition of LCA on Wikipedia: "The lowest common ancestor
# of two nodes p and q in a binary tree T is the lowest node that has both p
# and q as descendants (where we allow a node to be a descendant of itself)". A
# descendant of a node x is a node y that is on the path from node x to some
# leaf node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of
# itself according to the definition of LCA.
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
# Output: null
# Explanation: Node 10 does not exist in the tree, so return null.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# 
# 
# 
# Follow up: Can you find the LCA traversing the tree, without checking nodes
# existence?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target, path):
            if not root:
                return False
            path.append(root)
            if root == target:
                return True
            if dfs(root.left, target, path) or dfs(root.right, target, path):
                return True
            path.pop()
            return False

        lowest_common_ancestor = None        
        p_path = []
        dfs(root, p, p_path)
        if not p_path:
            return lowest_common_ancestor

        q_path = []
        dfs(root, q, q_path)
        
        if not q_path:
            return lowest_common_ancestor

        for i in range(min(len(q_path), len(p_path))):
            if q_path[i] == p_path[i]:
                lowest_common_ancestor = q_path[i]
                    
        return lowest_common_ancestor
# @lc code=end
