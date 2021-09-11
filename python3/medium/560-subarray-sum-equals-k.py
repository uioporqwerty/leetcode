#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.73%)
# Likes:    8767
# Dislikes: 296
# Total Accepted:    549K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# continuous subarrays whose sum equals to k.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        complements = {0:1}
        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num
            complement = current_sum - k
            ans += complements.get(complement, 0)
            complements[current_sum] = complements.get(current_sum, 0) + 1
                
        return ans
# @lc code=end
