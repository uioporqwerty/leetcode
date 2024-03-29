#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (37.55%)
# Likes:    15664
# Dislikes: 3388
# Total Accepted:    2.4M
# Total Submissions: 6.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
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
    def getListLength(self, head: ListNode) -> int:
        copy = head
        length = 0
        while copy:
            copy = copy.next
            length += 1 

        return length

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        sum_start = result
        
        # len_l1 = self.getListLength(l1)
        # len_l2 = self.getListLength(l2)
        
        # while l1 and len_l1 > len_l2:
        #     result.next = ListNode(l1.val)
        #     l1 = l1.next
        #     result = result.next
        #     len_l1 -= 1

        # while l2 and len_l2 > len_l1:
        #     result.next = ListNode(l2.val)
        #     l2 = l2.next 
        #     result = result.next
        #     len_l2 -= 1
        
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = 1 if total > 9 else 0
            result.next = ListNode(total % 10)
            result = result.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            carry = 1 if total > 9 else 0
            result.next = ListNode(total % 10)
            result = result.next
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            carry = 1 if total > 9 else 0
            result.next = ListNode(total % 10)
            result = result.next
            l2 = l2.next
        
        if carry:
            result.next = ListNode(carry)
        
        return sum_start.next


        
# @lc code=end
