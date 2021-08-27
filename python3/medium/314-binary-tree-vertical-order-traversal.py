#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (47.65%)
# Likes:    1651
# Dislikes: 215
# Total Accepted:    179.4K
# Total Submissions: 371.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left to
# right.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# 
# 
# Example 3:
# 
# 
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]
# 
# 
# Example 4:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
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
from collections import deque
from heapq import heappush, heappop

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        if not root:
            return []
        q = deque([(root, 0)])
        heap = []
        
        while q:
            for _ in range(len(q)):
                node, node_level = q.popleft()
                if node_level in levels:
                    levels[node_level].append(node.val)
                else:
                    levels[node_level] = [node.val]
                if node.left:
                    q.append((node.left, node_level - 1))
                if node.right:
                    q.append((node.right, node_level + 1))
        
        vertical_order = []
        for key in levels:
            heappush(heap, (key, levels[key]))
        
        while heap:
            _, nodes = heappop(heap)
            vertical_order.append(nodes)
        
        return vertical_order

# @lc code=end
