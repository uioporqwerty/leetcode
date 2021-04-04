#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (65.66%)
# Likes:    634
# Dislikes: 755
# Total Accepted:    123.5K
# Total Submissions: 187.8K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard like the image
# below.
#
# In the American keyboard:
#
#
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
#
#
#
# Example 1:
#
#
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
#
#
# Example 2:
#
#
# Input: words = ["omk"]
# Output: []
#
#
# Example 3:
#
#
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).
#
#
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row, second_row, third_row = (
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        )
        result = []
        for word in words:
            found_first_row, found_second_row, found_third_row = True, True, True
            for c in word:
                if c.lower() not in first_row:
                    found_first_row = False
                if c.lower() not in second_row:
                    found_second_row = False
                if c.lower() not in third_row:
                    found_third_row = False
            if found_first_row or found_second_row or found_third_row:
                result.append(word)

        return result


# @lc code=end
