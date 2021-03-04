#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (86.90%)
# Likes:    2513
# Dislikes: 399
# Total Accepted:    597.8K
# Total Submissions: 687.9K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".
#
#
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
#
#
# Constraints:
#
#
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
#
#
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(list(jewels))
        count = 0
        for i in range(len(stones)):
            if stones[i] in j:
                count += 1

        return count


# @lc code=end
