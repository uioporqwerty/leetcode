#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (69.11%)
# Likes:    2400
# Dislikes: 129
# Total Accepted:    156.3K
# Total Submissions: 224.2K
# Testcase Example:  '"a1b2"'
#
# Given a string s, we can transform every letter individually to be lowercase
# or uppercase to create another string.
# 
# Return a list of all possible strings we could create. You can return the
# output in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# 
# 
# Example 2:
# 
# 
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
# 
# 
# Example 3:
# 
# 
# Input: s = "12345"
# Output: ["12345"]
# 
# 
# Example 4:
# 
# 
# Input: s = "0"
# Output: ["0"]
# 
# 
# 
# Constraints:
# 
# 
# s will be a string with length between 1 and 12.
# s will consist only of letters or digits.
# 
# 
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(len(permutations)):
                    permutation = list(permutations[j])
                    permutation[i] = permutation[i].swapcase()
                    permutations.append(''.join(permutation))
        
        return permutations
# @lc code=end
