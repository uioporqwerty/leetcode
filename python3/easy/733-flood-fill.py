#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (55.88%)
# Likes:    1888
# Dislikes: 241
# Total Accepted:    227.5K
# Total Submissions: 406.3K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
#
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.  Replace the
# color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
#
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels
# connected
# by a path of the same color as the starting pixel are colored with the new
# color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected
# to the starting pixel.
#
#
#
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0  and 0 .
# The value of each color in image[i][j] and newColor will be an integer in [0,
# 65535].
#
#

# @lc code=start
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        num_rows, num_cols = len(image), len(image[0])
        q = deque([(sr, sc)])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        start_color = image[sr][sc]
        image[sr][sc] = newColor
        while q:
            for _ in range(len(q)):
                coord = q.popleft()
                neighbors = []
                delta_row = [-1, 0, 1, 0]
                delta_col = [0, 1, 0, -1]
                for i in range(len(delta_row)):
                    neighbor_row = coord[0] + delta_row[i]
                    neighbor_col = coord[1] + delta_col[i]
                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                        if image[neighbor_row][neighbor_col] == start_color:
                            neighbors.append((neighbor_row, neighbor_col))

                for neighbor in neighbors:
                    if visited[neighbor[0]][neighbor[1]]:
                        continue
                    image[neighbor[0]][neighbor[1]] = newColor
                    visited[neighbor[0]][neighbor[1]] = True
                    q.append((neighbor[0], neighbor[1]))

        return image


# @lc code=end
