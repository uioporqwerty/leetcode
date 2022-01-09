#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (41.88%)
# Likes:    4188
# Dislikes: 143
# Total Accepted:    402.2K
# Total Submissions: 960.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,1,1,2,3]
# Output: [2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode(-1)
        last_non_duplicate = None
        while head:
            nxt = head.next
            is_duplicate = False
            while nxt and nxt.val == head.val:
                nxt = nxt.next
                is_duplicate = True
            
            if not is_duplicate:
                if not s.next:
                    s.next = head
                last_non_duplicate = head
            else:
                if last_non_duplicate:
                    last_non_duplicate.next = nxt
            head = nxt
        
        return s.next
# @lc code=end
