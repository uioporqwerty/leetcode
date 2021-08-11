#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (45.02%)
# Likes:    6846
# Dislikes: 255
# Total Accepted:    435.5K
# Total Submissions: 960.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
#
#
# Example 4:
#
#
# Input: nums = [9,11], k = 2
# Output: [11]
#
#
# Example 5:
#
#
# Input: nums = [4,-2], k = 2
# Output: [4]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc code=start
from heapq import heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        heap = []
        window_start = 0

        for window_end in range(len(nums)):
            current_num = nums[window_end]
            window_length = window_end - window_start + 1

            heappush(heap, (-1 * current_num, window_end))

            if window_length >= k:
                while heap and heap[0][1] < window_start:
                    heappop(heap)

                maximums.append(-1 * heap[0][0])
                window_start += 1

        return maximums


# @lc code=end
