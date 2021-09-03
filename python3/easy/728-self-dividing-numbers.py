#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (75.98%)
# Likes:    964
# Dislikes: 334
# Total Accepted:    161.9K
# Total Submissions: 212.1K
# Testcase Example:  '1\n22'
#
# A self-dividing number is a number that is divisible by every digit it
# contains.
# 
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
# 
# 
# A self-dividing number is not allowed to contain the digit zero.
# 
# Given two integers left and right, return a list of all the self-dividing
# numbers in the range [left, right].
# 
# 
# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]
# 
# 
# Constraints:
# 
# 
# 1 <= left <= right <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def isSelfDividing(self, num: int) -> bool:
        original_num = num
        while num:
            digit = num % 10
            if digit == 0 or original_num % digit != 0:
                return False
            num //= 10
        
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        for i in range(left, right + 1):
            if self.isSelfDividing(i):
                self_dividing_numbers.append(i)
        
        return self_dividing_numbers
# @lc code=end
