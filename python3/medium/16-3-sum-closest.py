#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.30%)
# Likes:    3026
# Dislikes: 168
# Total Accepted:    565.3K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 =
# 2).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = -1
        closest_distance = float("inf")
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                current_distance = abs(target - current_sum)
                if current_distance < closest_distance:
                    closest_distance = current_distance
                    closest_sum = current_sum
                if current_sum < target:
                    j += 1
                else:
                    k -= 1

        return closest_sum


# @lc code=end
