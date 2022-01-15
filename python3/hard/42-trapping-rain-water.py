#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (55.15%)
# Likes:    16059
# Dislikes: 227
# Total Accepted:    991.6K
# Total Submissions: 1.8M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        right_walls = [0] * len(height)
        left_walls = [0] * len(height)

        max_left_wall = 0
        for i in range(len(height)):
            left_walls[i] = max_left_wall
            max_left_wall = max(max_left_wall, height[i])
        
        max_right_wall = 0
        for i in reversed(range(len(height))):
            right_walls[i] = max_right_wall
            max_right_wall = max(max_right_wall, height[i])
        
        total_water = 0
        for i in range(len(height)):
            elevation = height[i]
            lowest_wall = min(left_walls[i], right_walls[i])
            if lowest_wall > elevation:
                total_water += lowest_wall - elevation

        return total_water
# @lc code=end
