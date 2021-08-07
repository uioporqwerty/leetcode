#
# @lc app=leetcode id=1197 lang=python3
#
# [1197] Minimum Knight Moves
#
# https://leetcode.com/problems/minimum-knight-moves/description/
#
# algorithms
# Medium (38.23%)
# Likes:    824
# Dislikes: 270
# Total Accepted:    79.5K
# Total Submissions: 206.3K
# Testcase Example:  '2\n1'
#
# In an infinite chess board with coordinates from -infinity to +infinity, you
# have a knight at square [0, 0].
#
# A knight has 8 possible moves it can make, as illustrated below. Each move is
# two squares in a cardinal direction, then one square in an orthogonal
# direction.
#
#
#
# Return the minimum number of steps needed to move the knight to the square
# [x, y].  It is guaranteed the answer exists.
#
#
# Example 1:
#
#
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
#
#
# Example 2:
#
#
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#
#
#
# Constraints:
#
#
# |x| + |y| <= 300
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def getNeighbors(self, coord: (int, int)) -> [int]:
        row, col = coord
        delta_rows = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_cols = [-1, 1, 2, 2, 1, -1, -2, -2]
        neighbors = []
        for i in range(len(delta_rows)):
            neighbors.append((row + delta_rows[i], col + delta_cols[i]))

        return neighbors

    def minKnightMoves(self, x: int, y: int) -> int:
        moves = 0
        q = deque([(0, 0)])
        visited = set()

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == (x, y):
                    return moves
                for neighbor in self.getNeighbors(node):
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)
            moves += 1

        return moves


# @lc code=end
