#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
#
# algorithms
# Easy (67.92%)
# Likes:    748
# Dislikes: 106
# Total Accepted:    91.4K
# Total Submissions: 134.8K
# Testcase Example:  '["cat","bt","hat","tree"]\n"atach"'
#
# You are given an array of strings words and a string chars.
# 
# A string is good if it can be formed by characters from chars (each character
# can only be used once).
# 
# Return the sum of lengths of all good strings in words.
# 
# 
# Example 1:
# 
# 
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer
# is 3 + 3 = 6.
# 
# 
# Example 2:
# 
# 
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the
# answer is 5 + 5 = 10.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.
# 
# 
#

# @lc code=start
import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        character_count = [0] * 26
        for i in range(len(chars)):
            character_count[ord(chars[i]) - ord('a')] += 1
        
        length = 0
        for word in words:
            count_copy = copy.deepcopy(character_count)
            is_valid = True
            for c in word:
                if count_copy[ord(c) - ord('a')] == 0:
                    is_valid = False
                    break
                count_copy[ord(c) - ord('a')] -= 1
            if is_valid:
                length += len(word)
        
        return length


# @lc code=end
