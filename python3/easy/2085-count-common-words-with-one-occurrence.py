#
# @lc app=leetcode id=2085 lang=python3
#
# [2085] Count Common Words With One Occurrence
#
# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/
#
# algorithms
# Easy (71.07%)
# Likes:    196
# Dislikes: 5
# Total Accepted:    15.1K
# Total Submissions: 21.3K
# Testcase Example:  '["leetcode","is","amazing","as","is"]\n["amazing","leetcode","is"]'
#
# Given two string arrays words1 and words2, return the number of strings that
# appear exactly once in each of the two arrays.
# 
# 
# Example 1:
# 
# 
# Input: words1 = ["leetcode","is","amazing","as","is"], words2 =
# ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this
# string.
# - "amazing" appears exactly once in each of the two arrays. We count this
# string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it
# in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count
# this string.
# Thus, there are 2 strings that appear exactly once in each of the two
# arrays.
# 
# 
# Example 2:
# 
# 
# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.
# 
# 
# Example 3:
# 
# 
# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two
# arrays is "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words1.length, words2.length <= 1000
# 1 <= words1[i].length, words2[j].length <= 30
# words1[i] and words2[j] consists only of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_count = Counter(words1)
        words2_count = Counter(words2)
        common_words_count = 0

        for word in words2:
            if word in words1_count and words1_count[word] == 1 and words1_count[word] == words2_count[word]:
                common_words_count += 1
        
        return common_words_count
            
# @lc code=end
