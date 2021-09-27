#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (46.10%)
# Likes:    4987
# Dislikes: 443
# Total Accepted:    413.6K
# Total Submissions: 857.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# 
# 
# Example 4:
# 
# 
# Input: head = [1], k = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
# 
# 
# 
# Follow-up: Can you solve the problem in O(1) extra memory space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        copy = head
        gs = head
        prev_prev_gs = None
        current_gs = None
        list_start = None
        orig_k = k
        while copy:
            k -= 1
            copy = copy.next

            if k == 0:
                current_gs = gs
                prev_gs = None
                while current_gs != copy:
                    temp = current_gs.next
                    current_gs.next = prev_gs
                    prev_gs = current_gs
                    current_gs = temp
                k = orig_k
                if not list_start:
                    list_start = prev_gs
                if not prev_prev_gs:
                    gs.next = copy
                else:
                    prev_prev_gs.next = prev_gs
                
                prev_prev_gs = gs
                gs = copy

        if k != 0:
            prev_prev_gs.next = gs
            
        return list_start
# @lc code=end
