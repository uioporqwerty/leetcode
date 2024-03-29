#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (57.88%)
# Likes:    859
# Dislikes: 31
# Total Accepted:    55.5K
# Total Submissions: 95.9K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given an array intervals where intervals[i] = [li, ri] represent the interval
# [li, ri), remove all intervals that are covered by another interval in the
# list.
# 
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a
# and b <= d.
# 
# Return the number of remaining intervals.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[2,3]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= li <= ri <= 10^5
# All the given intervals are unique.
# 
# 
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        count = 0
        prev_end = 0

        for interval in intervals:
            if interval[1] > prev_end:
                count += 1
                prev_end = interval[1]
        
        return count

    #[[0,10],[5,12]]
    #ans[-1]
# @lc code=end
