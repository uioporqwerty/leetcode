#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (53.53%)
# Likes:    2429
# Dislikes: 127
# Total Accepted:    382.2K
# Total Submissions: 710.7K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: ["1"]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
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
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = self.dfs(root, [], [])
        return result

    def dfs(self, root: TreeNode, path=[], result=[]) -> List[str]:
        if root:
            path.append(str(root.val))
            if not root.left and not root.right:
                result.append("->".join(path))

            if root.left:
                self.dfs(root.left, path, result)
            if root.right:
                self.dfs(root.right, path, result)
            path.pop()
        return result


# @lc code=end
