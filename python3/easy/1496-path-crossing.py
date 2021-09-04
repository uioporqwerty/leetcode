#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#
# https://leetcode.com/problems/path-crossing/description/
#
# algorithms
# Easy (55.16%)
# Likes:    389
# Dislikes: 7
# Total Accepted:    29.8K
# Total Submissions: 54K
# Testcase Example:  '"NES"'
#
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
# moving one unit north, south, east, or west, respectively. You start at the
# origin (0, 0) on a 2D plane and walk on the path specified by path.
# 
# Return true if the path crosses itself at any point, that is, if at any time
# you are on a location you have previously visited. Return false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# 
# 
# Example 2:
# 
# 
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
# 
# 
# Constraints:
# 
# 
# 1 <= path.length <= 10^4
# path[i] is either 'N', 'S', 'E', or 'W'.
# 
# 
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0,0)])
        current_point = (0,0)
        for direction in path:
            if direction == "N":
                current_point = (current_point[0] + 1, current_point[1])
            elif direction == "S":
                current_point = (current_point[0] - 1, current_point[1])
            elif direction == "E":
                current_point = (current_point[0], current_point[1] + 1)
            else:
                current_point = (current_point[0], current_point[1] - 1)
            
            if current_point in visited:
                return True
            visited.add(current_point)
        
        return False
# @lc code=end
