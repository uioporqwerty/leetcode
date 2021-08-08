#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
#
# algorithms
# Easy (81.66%)
# Likes:    1460
# Dislikes: 78
# Total Accepted:    199.4K
# Total Submissions: 244K
# Testcase Example:  '[1,0,1]'
#
# Given head which is a reference node to a singly-linked list. The value of
# each node in the linked list is either 0 or 1. The linked list holds the
# binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
#
# Example 1:
#
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
#
# Example 2:
#
#
# Input: head = [0]
# Output: 0
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: 1
#
#
# Example 4:
#
#
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
#
#
# Example 5:
#
#
# Input: head = [0,0]
# Output: 0
#
#
#
# Constraints:
#
#
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head: ListNode) -> int:
        length = 0
        copy = head
        while copy:
            copy = copy.next
            length += 1
        return length

    def getDecimalValue(self, head: ListNode) -> int:
        list_length = self.getLength(head)
        value = 0

        while head:
            value += head.val * 2 ** (list_length - 1)
            head = head.next
            list_length -= 1

        return value


# @lc code=end
