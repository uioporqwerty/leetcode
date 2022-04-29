#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (61.36%)
# Likes:    1495
# Dislikes: 152
# Total Accepted:    95.3K
# Total Submissions: 153.8K
# Testcase Example:  '["cat","bat","rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other word to form another longer word - let's call this word successor. For
# example, when the root "an" is followed by the successor word "other", we can
# form a new word "another".
# 
# Given a dictionary consisting of many roots and a sentence consisting of
# words separated by spaces, replace all the successors in the sentence with
# the root forming it. If a successor can be replaced by more than one root,
# replace it with the root that has the shortest length.
# 
# Return the sentence after the replacement.
# 
# 
# Example 1:
# 
# 
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled
# by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# Example 2:
# 
# 
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 10^6
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one
# space.
# sentence does not have leading or trailing spaces.
# 
# 
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        
        # Build prefix tree
        for word in dictionary:
            
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWord = True
        
        sentence_words = sentence.split()
        
        # Search for Prefix
        for i in range(len(sentence_words)):
            word = sentence_words[i]
            
            cur = root
            for j in range(len(word)):
                c = word[j]
                if c not in cur.children:
                    break
                    
                if cur.children[c].isWord:
                    sentence_words[i] = word[0:j+1]# Prefix is a word so change and exit
                    break
                cur = cur.children[c]
        
        return ' '.join(sentence_words)
# @lc code=end
