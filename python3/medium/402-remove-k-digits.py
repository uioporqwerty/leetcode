# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (29.05%)
# Likes:    4280
# Dislikes: 180
# Total Accepted:    209.5K
# Total Submissions: 720.4K
# Testcase Example:  '"1432219"\n3'
#
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
# 
# 
# Example 1:
# 
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# Example 2:
# 
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# Example 3:
# 
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= num.length <= 10^5
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Brute Force
        # if k >= len(num):
        #     return "0"

        # smallest_num = float("inf")

        # def removeDigits(new_num: str, remainder: int):
        #     nonlocal smallest_num
        #     if remainder < 0 or not new_num:
        #         return
        #     val = int(new_num)
        #     smallest_num = min(smallest_num, val)
        #     for i in range(len(new_num)):
        #         removeDigits(new_num[:i] + new_num[i+1:], remainder - 1)
        
        # removeDigits(num, k)

        # return str(smallest_num)

        s = []

        for digit in num:
            while k and s and s[-1] > digit:
                s.pop()
                k -= 1

            s.append(digit)

        result = s[:-k] if k else s

        return "".join(result).lstrip("0") or "0"

# @lc code=end
