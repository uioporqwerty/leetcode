#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (67.22%)
# Likes:    1260
# Dislikes: 73
# Total Accepted:    126.7K
# Total Submissions: 186.8K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# 
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# 
# 
# 
# Constraints:
# 
# 
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []

        if not root:
            return levels 

        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                for child in node.children:
                    q.append(child)

                level.append(node.val)
            levels.append(level)

        return levels       
# @lc code=end
