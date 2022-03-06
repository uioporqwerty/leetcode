#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#
# https://leetcode.com/problems/buildings-with-an-ocean-view/description/
#
# algorithms
# Medium (81.10%)
# Likes:    665
# Dislikes: 96
# Total Accepted:    87K
# Total Submissions: 108.2K
# Testcase Example:  '[4,2,3,1]'
#
# There are n buildings in a line. You are given an integer array heights of
# size n that represents the heights of the buildings in the line.
# 
# The ocean is to the right of the buildings. A building has an ocean view if
# the building can see the ocean without obstructions. Formally, a building has
# an ocean view if all the buildings to its right have a smaller height.
# 
# Return a list of indices (0-indexed) of buildings that have an ocean view,
# sorted in increasing order.
# 
# 
# Example 1:
# 
# 
# Input: heights = [4,2,3,1]
# Output: [0,2,3]
# Explanation: Building 1 (0-indexed) does not have an ocean view because
# building 2 is taller.
# 
# 
# Example 2:
# 
# 
# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]
# Explanation: All the buildings have an ocean view.
# 
# 
# Example 3:
# 
# 
# Input: heights = [1,3,2,4]
# Output: [3]
# Explanation: Only building 3 has an ocean view.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = []
        max_height = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                output.append(i)
            max_height = max(max_height, heights[i])
        
        return output[::-1]
# @lc code=end
