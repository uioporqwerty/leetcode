#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (45.68%)
# Likes:    6254
# Dislikes: 228
# Total Accepted:    583.8K
# Total Submissions: 1.3M
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        
        indegrees = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}
        
        # Build graph
        for course in prerequisites:
            parent, child = course[0], course[1]
            graph[parent].append(child)
            indegrees[child] += 1
        
        sources = deque()
        for key in graph:
            if indegrees[key] == 0:
                sources.append(key)
        
        while sources:
            vertex = sources.popleft()
            order.append(vertex)
            
            for child in graph[vertex]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    sources.append(child)
        
        if len(order) != numCourses:
            return []
        
        return reversed(order)
# @lc code=end
