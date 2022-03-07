#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (63.90%)
# Likes:    2062
# Dislikes: 168
# Total Accepted:    195.5K
# Total Submissions: 304.7K
# Testcase Example:  '[4,2,5,1,3]'
#
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in
# place.
# 
# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly linked
# list, the predecessor of the first element is the last element, and the
# successor of the last element is the first element.
# 
# We want to do the transformation in place. After the transformation, the left
# pointer of the tree node should point to its predecessor, and the right
# pointer should point to its successor. You should return the pointer to the
# smallest element of the linked list.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [4,2,5,1,3]
# 
# 
# Output: [1,2,3,4,5]
# 
# Explanation: The figure below shows the transformed BST. The solid line
# indicates the successor relationship, while the dashed line means the
# predecessor relationship.
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,3]
# Output: [1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# All the values of the tree are unique.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # O(n) time O(n) space
        nodes = []
        if not root:
            return None

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)

        inorder(root)
        nodes[0].left = nodes[-1]
        
        for i in range(1, len(nodes)):
            nodes[i - 1].right = nodes[i]
            nodes[i].left = nodes[i - 1]

        nodes[len(nodes) - 1].right = nodes[0]

        return nodes[0]
# @lc code=end
