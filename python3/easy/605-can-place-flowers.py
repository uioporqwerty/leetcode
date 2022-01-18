#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (32.00%)
# Likes:    2086
# Dislikes: 559
# Total Accepted:    230.4K
# Total Submissions: 715.2K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule.
# 
# 
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
# 
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 0 and i == 0: #Front
                flowerbed[i] = 1
                n -= 1
            elif i - 1 > 0 and i + 1 < len(flowerbed) and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0: #Middle
                flowerbed[i] = 1
                n -= 1
            elif i - 1 >= 0 and flowerbed[i - 1] == 0 and i == len(flowerbed) - 1: #Last
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
# @lc code=end
