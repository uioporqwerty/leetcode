#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
# https://leetcode.com/problems/most-common-word/description/
#
# algorithms
# Easy (45.44%)
# Likes:    1059
# Dislikes: 2247
# Total Accepted:    247.3K
# Total Submissions: 545.1K
# Testcase Example:  '"Bob hit a ball, the hit BALL flew far after it was hit."\n["hit"]'
#
# Given a string paragraph and a string array of the banned words banned,
# return the most frequent word that is not banned. It is guaranteed there is
# at least one word that is not banned, and that the answer is unique.
# 
# The words in paragraph are case-insensitive and the answer should be returned
# in lowercase.
# 
# 
# Example 1:
# 
# 
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent
# non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is
# banned.
# 
# 
# Example 2:
# 
# 
# Input: paragraph = "a.", banned = []
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols:
# "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        word_counts = Counter(words)
        banned_words = set(banned)
        max_seen, max_word = 0, ''

        for word in word_counts:
            if word not in banned_words and word_counts[word] > max_seen:
                max_word = word
                max_seen = word_counts[word]
        
        return max_word

# @lc code=end
