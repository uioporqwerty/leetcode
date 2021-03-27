#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (42.96%)
# Likes:    1149
# Dislikes: 1650
# Total Accepted:    127.9K
# Total Submissions: 297.2K
# Testcase Example:  '[1,2,1]'
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following
# steps:
#
#
# Add one piece of fruit from this tree to your baskets.  If you cannot,
# stop.
# Move to the next tree to the right of the current tree.  If there is no tree
# to the right, stop.
#
#
# Note that you do not have any choice after the initial choice of starting
# tree: you must perform step 1, then step 2, then back to step 1, then step 2,
# and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit, but
# you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?
#
#
#
# Example 1:
#
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
#
#
#
# Example 2:
#
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
#
#
#
# Example 3:
#
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
#
#
#
# Example 4:
#
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4
# fruits.
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
#
#
#

# @lc code=start
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket = {}
        window_start, window_fruit_total = 0, 0
        max_fruit = 0
        for window_end in range(len(tree)):
            if tree[window_end] not in basket:
                basket[tree[window_end]] = 1
            else:
                basket[tree[window_end]] += 1

            window_fruit_total += 1
            while len(basket) > 2:
                window_fruit_total -= 1
                if basket[tree[window_start]] == 1:
                    del basket[tree[window_start]]
                else:
                    basket[tree[window_start]] -= 1
                window_start += 1
            max_fruit = max(max_fruit, window_fruit_total)

        return max_fruit


# @lc code=end
