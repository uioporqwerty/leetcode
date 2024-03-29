#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (35.72%)
# Likes:    3405
# Dislikes: 274
# Total Accepted:    387.4K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
# Example 3:
#
#
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
#
#
# Example 4:
#
#
# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
#
#
# Example 5:
#
#
# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^5
# intervals is sorted by intervals[i][0] in ascending order.
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def hasOverlap(self, interval1: List[int], interval2: List[int]) -> bool:
        return interval1[1] >= interval2[0] and interval2[1] >= interval1[0]

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort()

        ans = []

        for interval in intervals:
            if not ans or not self.hasOverlap(ans[-1], interval):
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans


# @lc code=end
