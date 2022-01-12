#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#
# https://leetcode.com/problems/plus-one-linked-list/description/
#
# algorithms
# Medium (60.08%)
# Likes:    740
# Dislikes: 39
# Total Accepted:    64.2K
# Total Submissions: 106.8K
# Testcase Example:  '[1,2,3]'
#
# Given a non-negative integer represented as a linked list of digits, plus one
# to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
# 
# 
# Example 1:
# Input: head = [1,2,3]
# Output: [1,2,4]
# Example 2:
# Input: head = [0]
# Output: [1]
# 
# 
# Constraints:
# 
# 
# The number of nodes in the linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# The number represented by the linked list does not contain leading zeros
# except for the zero itself. 
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
    def reverse(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev

    def plusOne(self, head: ListNode) -> ListNode:
        reverse_start = self.reverse(head)
        total = reverse_start.val + 1
        carry = 1 if total > 9 else 0
        reverse_start.val = total % 10
        prev = reverse_start
        copy = reverse_start.next
        
        while carry and copy:
            prev = copy
            total = copy.val + carry
            carry = 1 if total > 9 else 0
            copy.val = total % 10
            copy = copy.next
        
        if carry:
            prev.next = ListNode(carry)
        
        original = self.reverse(reverse_start)
        
        return original

# @lc code=end
