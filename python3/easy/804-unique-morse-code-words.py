#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#
# https://leetcode.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (78.85%)
# Likes:    897
# Dislikes: 821
# Total Accepted:    180.2K
# Total Submissions: 228.1K
# Testcase Example:  '["gin", "zen", "gig", "msg"]'
#
# International Morse Code defines a standard encoding where each letter is
# mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps
# to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
#
#
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# Now, given a list of words, each word can be written as a concatenation of
# the Morse code of each letter. For example, "cab" can be written as
# "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call
# such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
#
#
# Note:
#
#
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.
#
#
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_lookup = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        unique_representations = set()
        for word in words:
            word_morse_letters = []
            for c in word:
                word_morse_letters.append(morse_code_lookup[ord(c) - ord("a")])
            morse_word = "".join(word_morse_letters)
            unique_representations.add(morse_word)

        return len(unique_representations)


# @lc code=end
