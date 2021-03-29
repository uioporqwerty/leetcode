#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#
# https://leetcode.com/problems/goal-parser-interpretation/description/
#
# algorithms
# Easy (85.50%)
# Likes:    225
# Dislikes: 26
# Total Accepted:    42.1K
# Total Submissions: 49.4K
# Testcase Example:  '"G()(al)"'
#
# You own a Goal Parser that can interpret a string command. The command
# consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal
# Parser will interpret "G" as the string "G", "()" as the string "o", and
# "(al)" as the string "al". The interpreted strings are then concatenated in
# the original order.
#
# Given the string command, return the Goal Parser's interpretation of
# command.
#
#
# Example 1:
#
#
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
#
#
# Example 2:
#
#
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
#
#
# Example 3:
#
#
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
#
#
#
# Constraints:
#
#
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.
#
#
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        result = []
        for i in range(len(command)):
            if command[i] == "G":
                result.append("G")
            elif i + 1 < len(command) and command[i] == "(" and command[i + 1] == ")":
                result.append("o")
            elif i + 1 < len(command) and command[i] == "(" and command[i + 1] == "a":
                result.append("al")

        return "".join(result)


# @lc code=end
