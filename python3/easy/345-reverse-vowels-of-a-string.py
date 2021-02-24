#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (45.05%)
# Likes:    923
# Dislikes: 1421
# Total Accepted:    263.3K
# Total Submissions: 584.5K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#
#
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_arr = list(s)
        i, j = 0, len(s_arr) - 1
        vowels = set(["a", "e", "i", "o", "u"])

        while i < j:
            while i < j and s_arr[i].lower() not in vowels:
                i += 1
            while i < j and s_arr[j].lower() not in vowels:
                j -= 1
            s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
            i += 1
            j -= 1

        return "".join(s_arr)


# @lc code=end
