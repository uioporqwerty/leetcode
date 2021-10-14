#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (41.14%)
# Likes:    4547
# Dislikes: 228
# Total Accepted:    401.3K
# Total Submissions: 950.9K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [5], left = 1, right = 1
# Output: [5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# 
# 
# 
# Follow up: Could you do it in one pass?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        rs, ps, pe = None, None, None
        copy = head
        curr_pos = 1
        while copy:
            if curr_pos == left:
                rs = copy
                prev = None
                while curr_pos != right:
                    nxt = copy.next
                    copy.next = prev
                    prev = copy
                    copy = nxt
                    curr_pos += 1
                pe = copy.next
                copy.next = prev
                if ps:
                    ps.next = copy
                    rs.next = pe
                    break
                else:
                    ps = copy
                    rs.next = pe
                    return ps
            ps = copy
            copy = copy.next
            curr_pos += 1
        
        return head
        
# @lc code=end
