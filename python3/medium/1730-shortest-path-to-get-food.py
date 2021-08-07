#
# @lc app=leetcode id=1730 lang=python3
#
# [1730] Shortest Path to Get Food
#
# https://leetcode.com/problems/shortest-path-to-get-food/description/
#
# algorithms
# Medium (55.34%)
# Likes:    145
# Dislikes: 7
# Total Accepted:    8.1K
# Total Submissions: 14.7K
# Testcase Example:  '[["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]'
#
# You are starving and you want to eat food as quickly as possible. You want to
# find the shortest path to arrive at any food cell.
#
# You are given an m x n character matrix, grid, of these different types of
# cells:
#
#
# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
#
#
# You can travel to any adjacent cell north, east, south, or west of your
# current location if there is not an obstacle.
#
# Return the length of the shortest path for you to reach any food cell. If
# there is no path for you to reach food, return -1.
#
#
# Example 1:
#
#
# Input: grid =
# [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
#
#
# Example 2:
#
#
# Input: grid =
# [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
#
#
# Example 3:
#
#
# Input: grid =
# [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach
# the bottom food.
#
# Example 4:
#
#
# Input: grid = [["O","*"],["#","O"]]
# Output: 2
#
#
# Example 5:
#
#
# Input: grid = [["X","*"],["#","X"]]
# Output: -1
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[row][col] is '*', 'X', 'O', or '#'.
# The grid contains exactly one '*'.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def getLocation(self, grid: List[List[str]]) -> (int, int):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                coord = (row, col)
                if grid[row][col] == "*":
                    return coord
        return None

    def getNeighbors(self, grid: List[List[str]], coord: (int, int)) -> List[str]:
        row, col = coord
        num_rows, num_cols = len(grid), len(grid[0])
        neighbors = []
        delta_rows = [-1, 0, 1, 0]
        delta_cols = [0, 1, 0, -1]

        for i in range(len(delta_rows)):
            neighbor_row = row + delta_rows[i]
            neighbor_col = col + delta_cols[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                neighbors.append((neighbor_row, neighbor_col))

        return neighbors

    def getFood(self, grid: List[List[str]]) -> int:
        current_location = self.getLocation(grid)

        q = deque([current_location])
        visited = set([current_location])
        current_length = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for neighbor in self.getNeighbors(grid, node):
                    if grid[neighbor[0]][neighbor[1]] == "#":
                        return current_length
                    if neighbor in visited or grid[neighbor[0]][neighbor[1]] == "X":
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)
            current_length += 1

        return -1


# @lc code=end
