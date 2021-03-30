#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (47.37%)
# Likes:    984
# Dislikes: 670
# Total Accepted:    213.5K
# Total Submissions: 448.2K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last in first out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal queue (push,
# top, pop, and empty).
#
# Implement the MyStack class:
#
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a queue, which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue), as long as you
# use only a queue's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
#
#
#
# Follow-up: Can you implement the stack such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer. You can
# use more than two queues.
#
#

# @lc code=start
from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while self.q:
            self.q2.appendleft(self.q.popleft())

        val = self.q2.popleft()
        while self.q2:
            self.q.append(self.q2.pop())

        return val

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
