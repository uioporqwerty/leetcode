#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (52.54%)
# Likes:    2168
# Dislikes: 195
# Total Accepted:    267K
# Total Submissions: 504.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the sum of all left leaves.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and
# 15 respectively.
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
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

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        if not root:
            return total
        q = deque([(root, False)])
        while q:
            for i in range(len(q)):
                node, is_left = q.popleft()
                if node != root and not node.left and not node.right and is_left:
                    total += node.val
                if node.left:
                    q.append((node.left, True))
                if node.right:
                    q.append((node.right, False))
        
        return total
# @lc code=end
