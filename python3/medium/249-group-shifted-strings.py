#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (61.85%)
# Likes:    1230
# Dislikes: 226
# Total Accepted:    157.1K
# Total Submissions: 249.4K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# We can shift a string by shifting each of its letters to its successive
# letter.
# 
# 
# For example, "abc" can be shifted to be "bcd".
# 
# 
# We can keep shifting the string to form a sequence.
# 
# 
# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd"
# -> ... -> "xyz".
# 
# 
# Given an array of strings strings, group all strings[i] that belong to the
# same shifting sequence. You may return the answer in any order.
# 
# 
# Example 1:
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
# Example 2:
# Input: strings = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifts = {}
        shifts[strings[0]] = [strings[0]]

        for i in range(1, len(strings)):
            permutation = list(strings[i])
            found = False
            for _ in range(27):
                for k in range(len(permutation)):
                    next_ord = (ord(permutation[k]) + 1) % (ord('z') + 1) 
                    if next_ord < 97:
                        next_ord += 97
                    permutation[k] = chr(next_ord)
                modified = ''.join(permutation)
                if modified in shifts:
                    shifts[modified].append(strings[i])
                    found = True
                    break
            if not found:
                shifts[strings[i]] = [strings[i]]
        
        return [shifts[key] for key in shifts]

# @lc code=end
