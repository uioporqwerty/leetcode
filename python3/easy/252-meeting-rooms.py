#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (55.73%)
# Likes:    1037
# Dislikes: 53
# Total Accepted:    204.7K
# Total Submissions: 366.2K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
#
#
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
#
#
#

# @lc code=start
class Solution:
    def hasOverlap(self, interval1, interval2):
        merged_start = max(interval1[0], interval2[0])
        merged_end = min(interval1[1], interval2[1])
        print(interval1)
        print(interval2)
        print(merged_start)
        print(merged_end)
        return merged_end - merged_start > 0

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            if self.hasOverlap(intervals[i - 1], intervals[i]):
                return False

        return True


# @lc code=end
