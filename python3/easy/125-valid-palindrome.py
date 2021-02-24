#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (38.18%)
# Likes:    1767
# Dislikes: 3594
# Total Accepted:    795.5K
# Total Submissions: 2.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1

        return True


# @lc code=end
