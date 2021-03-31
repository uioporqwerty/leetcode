#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#
# https://leetcode.com/problems/two-sum-less-than-k/description/
#
# algorithms
# Easy (60.83%)
# Likes:    499
# Dislikes: 55
# Total Accepted:    58.7K
# Total Submissions: 96.4K
# Testcase Example:  '[34,23,1,24,75,33,54,8]\n60'
#
# Given an array nums of integers and integer k, return the maximum sum such
# that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j
# exist satisfying this equation, return -1.
#
#
# Example 1:
#
#
# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.
#
#
# Example 2:
#
#
# Input: nums = [10,20,30], k = 15
# Output: -1
# Explanation: In this case it is not possible to get a pair sum less that
# 15.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
# 1 <= k <= 2000
#
#
#

# @lc code=start
"""
map = {
    26: 34,
    37: 23,
    59: 1,
    36: 24
}
60-34 = 25
60-23=37
60-1=59
60-24=36
"""


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        nums.sort()
        start = 0
        end = len(nums) - 1
        max_sum = -1
        while start < end:
            total = nums[start] + nums[end]
            if total < k:
                max_sum = max(max_sum, total)
                start += 1
            else:
                end -= 1

        return max_sum


# @lc code=end
