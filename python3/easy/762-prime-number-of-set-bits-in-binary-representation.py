#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
#
# algorithms
# Easy (64.84%)
# Likes:    371
# Dislikes: 421
# Total Accepted:    59.8K
# Total Submissions: 91.4K
# Testcase Example:  '6\n10'
#
# Given two integers left and right, return the count of numbers in the
# inclusive range [left, right] having a prime number of set bits in their
# binary representation.
# 
# Recall that the number of set bits an integer has is the number of 1's
# present when written in binary.
# 
# 
# For example, 21 written in binary is 10101 which has 3 set bits.
# 
# 
# 
# Example 1:
# 
# 
# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# 
# 
# Example 2:
# 
# 
# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 
# 
# 
# Constraints:
# 
# 
# 1 <= left <= right <= 10^6
# 0 <= right - left <= 10^4
# 
# 
#

# @lc code=start
from math import sqrt
class Solution:
    def isPrime(self, num: int) -> bool:
        if num > 1:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        return False
    def countSetBits(self, num: int) -> int:
        count = 0
        while num:
            count += 1
            num &= (num - 1)
        
        return count

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            count_bits = self.countSetBits(i)
            if self.isPrime(count_bits):
                count += 1
        
        return count
# @lc code=end
