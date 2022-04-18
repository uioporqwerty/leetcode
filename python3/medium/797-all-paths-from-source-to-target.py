#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (80.47%)
# Likes:    3992
# Dislikes: 115
# Total Accepted:    273K
# Total Submissions: 337.6K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
# 
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node
# graph[i][j]).
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Example 2:
# 
# 
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# 
# 
# 
# Constraints:
# 
# 
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []
        
        def backtrack(node, path):
            if node == target:
                results.append(list(path))
                return
            for childNode in graph[node]:
                path.append(childNode)
                backtrack(childNode, path)
                path.pop()
        
        path = deque([0])
        backtrack(0, path)
        
        return results
        
# @lc code=end
