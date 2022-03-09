#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (46.86%)
# Likes:    2333
# Dislikes: 137
# Total Accepted:    155.8K
# Total Submissions: 329.2K
# Testcase Example:  '2736'
#
# You are given an integer num. You can swap two digits at most once to get the
# maximum valued number.
# 
# Return the maximum valued number you can get.
# 
# 
# Example 1:
# 
# 
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# Example 2:
# 
# 
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        # O(N) time O(N) space
        nums_list=list(str(num))
        maxes = [0] * len(nums_list)
        max_num = float("-inf")
        max_num_index = len(maxes) - 1
        for i in range(len(nums_list) - 1, -1, -1):
            digit = int(nums_list[i])
            if digit > max_num:
                max_num_index = i
                max_num = digit
            maxes[i] = max_num_index
        
        for i in range(len(nums_list)):
            digit = int(nums_list[i])
            next_max = int(nums_list[maxes[i]])
            if digit < next_max:
                nums_list[i], nums_list[maxes[i]] = nums_list[maxes[i]], nums_list[i]
                break
        

        return int(''.join(nums_list))
# @lc code=end
