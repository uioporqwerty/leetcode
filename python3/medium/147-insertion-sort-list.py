#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (48.10%)
# Likes:    1796
# Dislikes: 778
# Total Accepted:    272K
# Total Submissions: 565.5K
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a singly linked list, sort the list using insertion sort,
# and return the sorted list's head.
# 
# The steps of the insertion sort algorithm:
# 
# 
# Insertion sort iterates, consuming one input element each repetition and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list and inserts it
# there.
# It repeats until no input elements remain.
# 
# 
# The following is a graphical example of the insertion sort algorithm. The
# partially sorted list (black) initially contains only the first element in
# the list. One element (red) is removed from the input data and inserted
# in-place into the sorted list with each iteration.
# 
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000
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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        s = ListNode(-1)
        s.next = head
        tail = head
        nxt = head.next
        head.next = None
        head = nxt

        while head:
            copy = s.next
            prev = copy
            nxt = head.next
                
            while copy and copy.val < head.val:
                prev = copy
                copy = copy.next
            
            if not copy: # Insert at end
                tail.next = head
                tail = head
                tail.next = None
            elif copy == s.next: # Insert at head
                if s.next == tail:
                    s.next.next = None
                head.next = s.next
                s.next = head
            else:
                prev_next = prev.next
                prev.next = head
                head.next = prev_next

            head = nxt

        return s.next    

# @lc code=end
