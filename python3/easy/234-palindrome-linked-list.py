#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (40.42%)
# Likes:    4669
# Dislikes: 424
# Total Accepted:    560.7K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        copy = head

        while copy:
            next = copy.next
            copy.next = prev
            prev = copy
            copy = next

        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        middle_node = self.getMiddle(head)
        reverse_start = self.reverse(middle_node)

        while head and reverse_start:
            if head.val != reverse_start.val:
                return False
            head = head.next
            reverse_start = reverse_start.next

        return True


# @lc code=end
