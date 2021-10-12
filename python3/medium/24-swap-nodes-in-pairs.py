#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (54.13%)
# Likes:    4339
# Dislikes: 230
# Total Accepted:    666.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = head, head.next
        prev_pair_end = None
        list_start = ListNode(-1, curr)

        while curr:
            next_pair_start = curr.next
            curr.next = prev
            prev.next = next_pair_start
            if prev_pair_end:
                prev_pair_end.next = curr
            prev_pair_end = prev
            prev = prev.next
            curr = prev.next if prev else None
        
        return list_start.next

# @lc code=end
