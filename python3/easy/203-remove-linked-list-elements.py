#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (39.18%)
# Likes:    2452
# Dislikes: 119
# Total Accepted:    436.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        copy = head

        while copy and copy.val == val:
            copy = copy.next
        start = copy

        while copy:
            if copy.val == val:
                prev.next = copy.next
            else:
                prev = copy
            copy = copy.next

        return start


# @lc code=end
