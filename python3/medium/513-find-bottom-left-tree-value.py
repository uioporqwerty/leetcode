#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (62.54%)
# Likes:    1305
# Dislikes: 173
# Total Accepted:    128.9K
# Total Submissions: 205.1K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root:
            q = deque([root])
            left_val = 0
            while q:
                first_element = False

                for _ in range(len(q)):
                    node = q.popleft()
                    if not first_element:
                        left_val = node.val
                        first_element = True

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        return left_val


# @lc code=end
