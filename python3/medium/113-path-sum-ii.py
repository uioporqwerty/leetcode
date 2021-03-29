#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (49.04%)
# Likes:    2640
# Dislikes: 85
# Total Accepted:    403.3K
# Total Submissions: 816.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where each path's sum equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        allPaths = []
        self.dfs(root, targetSum, 0, allPaths, [])
        return allPaths

    def dfs(
        self,
        root: TreeNode,
        targetSum: int,
        currentSum: int,
        allPaths: List[List[int]],
        currentPath: List[int],
    ):
        if root:
            currentPath.append(root.val)
            currentSum += root.val
            if not root.left and not root.right and currentSum == targetSum:
                allPaths.append(list(currentPath))
            self.dfs(root.left, targetSum, currentSum, allPaths, currentPath)
            self.dfs(root.right, targetSum, currentSum, allPaths, currentPath)
            currentPath.pop()


# @lc code=end
