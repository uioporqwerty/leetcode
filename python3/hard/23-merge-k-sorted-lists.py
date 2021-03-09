#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (42.63%)
# Likes:    6658
# Dislikes: 345
# Total Accepted:    832.6K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#
# Constraints:
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __lt__(self, other):
#         return self.val < other.val
from heapq import *


def __lt__(self, other):
    return self.val < other.val


ListNode.__lt__ = __lt__


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        resultHead = None
        heap = []
        for lst in lists:
            if lst:
                heappush(heap, (lst.val, lst))

        while heap:
            node = heappop(heap)
            if not resultHead:
                resultHead = node[1]

            if node[1].next:
                next = node[1].next
                heappush(heap, (next.val, next))

            if heap:
                node[1].next = heap[0][1]

        return resultHead


# @lc code=end
