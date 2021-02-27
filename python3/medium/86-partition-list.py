#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (43.34%)
# Likes:    1853
# Dislikes: 374
# Total Accepted:    249.7K
# Total Submissions: 575.3K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_start, greater_start = None, None
        less, greater = None, None

        while head:
            if head.val < x:
                if not less:
                    less = head
                    less_start = less
                else:
                    less.next = head
                    less = head
            else:
                if not greater:
                    greater = head
                    greater_start = greater
                else:
                    greater.next = head
                    greater = head
            head = head.next

        if greater:
            greater.next = None
        if less:
            less.next = greater_start

        return less_start if less_start else greater_start


# @lc code=end
