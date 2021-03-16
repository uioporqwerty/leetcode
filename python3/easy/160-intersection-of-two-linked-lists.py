#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (43.14%)
# Likes:    5238
# Dislikes: 588
# Total Accepted:    629.2K
# Total Submissions: 1.4M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# It is guaranteed that there are no cycles anywhere in the entire linked
# structure.
#
# Note that the linked lists must retain their original structure after the
# function returns.
#
#
# Example 1:
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
#
#
# Example 2:
#
#
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
#
#
# Example 3:
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
# Constraints:
#
#
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 1 <= skipA <= m
# 1 <= skipB <= n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB
# intersect.
#
#
#
# Follow up: Could you write a solution that runs in O(n) time and use only
# O(1) memory?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getListLength(self, head: ListNode) -> int:
        copy = head
        length = 0
        while copy:
            length += 1
            copy = copy.next
        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        head_a_length = self.getListLength(headA)
        head_b_length = self.getListLength(headB)
        difference = max(head_a_length, head_b_length) - min(
            head_a_length, head_b_length
        )
        longer_list_head = headA if head_a_length >= head_b_length else headB
        smaller_list_head = headA if longer_list_head == headB else headB

        while longer_list_head and difference != 0:
            difference -= 1
            longer_list_head = longer_list_head.next

        while smaller_list_head and longer_list_head:
            if longer_list_head == smaller_list_head:
                return longer_list_head
            smaller_list_head = smaller_list_head.next
            longer_list_head = longer_list_head.next

        return None


# @lc code=end
