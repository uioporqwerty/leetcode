#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (40.56%)
# Likes:    2891
# Dislikes: 141
# Total Accepted:    306.7K
# Total Submissions: 755.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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

    def reorderList(self, head: ListNode) -> None:
        middle_node = self.getMiddle(head)
        l1 = head
        l2 = self.reverse(middle_node)
        is_alternate = False

        while l1 and l2 and l1 != l2 and l1.next != l2 and l2.next != l1:
            if not is_alternate:
                next = l1.next
                l1.next = l2
                l1 = next
            else:
                next = l2.next
                l2.next = l1
                l2 = next
            is_alternate = not is_alternate


# @lc code=end
