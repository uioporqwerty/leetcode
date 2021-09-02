#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (69.83%)
# Likes:    1596
# Dislikes: 64
# Total Accepted:    179K
# Total Submissions: 254.9K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given a n-ary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
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
# Output: 3
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The total number of nodes is in the range [0, 10^4].
# The depth of the n-ary tree is less than or equal to 1000.
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
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 1
        q = deque([root])
        max_depth = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.children:
                    max_depth = depth
                for child in node.children:
                    q.append(child)
            depth += 1
        return max_depth
# @lc code=end
