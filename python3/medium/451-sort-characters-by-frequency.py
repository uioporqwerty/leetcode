#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (64.35%)
# Likes:    2200
# Dislikes: 145
# Total Accepted:    244K
# Total Submissions: 378.6K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#

# @lc code=start
from collections import Counter
from heapq import *


class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = Counter(s)
        heap = []
        for frequency in frequencies:
            heappush(heap, (-frequencies[frequency], frequency))

        result = []
        while heap:
            letter_frequency, letter = heappop(heap)
            result.append(letter * -letter_frequency)

        return "".join(result)


# @lc code=end
