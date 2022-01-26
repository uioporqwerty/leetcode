#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (78.62%)
# Likes:    1419
# Dislikes: 48
# Total Accepted:    113.3K
# Total Submissions: 144K
# Testcase Example:  '[2,1,4]\n[1,0,3]'
#
# Given two binary search trees root1 and root2, return a list containing all
# the integers from both trees sorted in ascending order.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(root: TreeNode, lst: List[int]):
            if not root:
                return
            
            dfs(root.left, lst)
            lst.append(root.val)
            dfs(root.right, lst)
        
        lst1 = []
        dfs(root1, lst1)
        
        lst2 = []
        dfs(root2, lst2)

        i, j = 0, 0
        result = []

        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                result.append(lst1[i])
                i += 1
            else:
                result.append(lst2[j])
                j += 1

        while i < len(lst1):
            result.append(lst1[i])
            i += 1
        
        while j < len(lst2):
            result.append(lst2[j])
            j += 1

        return result
# @lc code=end
