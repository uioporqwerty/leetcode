#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (58.73%)
# Likes:    763
# Dislikes: 42
# Total Accepted:    76.1K
# Total Submissions: 129.2K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
#
#
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: "ab-cd"
# Output: "dc-ba"
#
#
#
# Example 2:
#
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
#
#
# Example 3:
#
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
#
#
#
# Note:
#
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "
#
#
#
#
#
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        arr = list(S)
        i = 0
        j = len(arr) - 1

        while i < j:
            while i < j and not arr[i].isalpha():
                i += 1
            while i < j and not arr[j].isalpha():
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return "".join(arr)


# @lc code=end
