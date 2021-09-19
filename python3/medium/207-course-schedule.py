#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.44%)
# Likes:    6849
# Dislikes: 283
# Total Accepted:    656.1K
# Total Submissions: 1.5M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses

        for i in range(len(prerequisites)):
            _, course = prerequisites[i]
            indegrees[course] += 1
        
        q = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for i in range(len(prerequisites)):
                prereq, course = prerequisites[i]
                if prereq == node:
                    indegrees[course] -= 1
                    if indegrees[course] == 0:
                        q.append(course)
            
        for i in range(len(indegrees)):
            if indegrees[i] != 0:
                return False
        return True
# @lc code=end
