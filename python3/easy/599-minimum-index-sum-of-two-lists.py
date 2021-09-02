#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (52.23%)
# Likes:    914
# Dislikes: 266
# Total Accepted:    125.4K
# Total Submissions: 238.2K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n' +'["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings.
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# Example 1:
# 
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# Example 2:
# 
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# Example 3:
# 
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
# 
# 
# Example 4:
# 
# 
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
# 
# 
# Example 5:
# 
# 
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the stings of list1 are unique.
# All the stings of list2 are unique.
# 
# 
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      restaurants_1 = set(list1)
      restaurants_2 = set(list2)
      counts = { }
      for i in range(len(list1)):
        counts[list1[i]] = i
      min_index = float("inf")
      common_restaurants = []
      for i in range(len(list2)):
        if list2[i] in counts:
          counts[list2[i]] = counts[list2[i]] + i
          min_index = min(min_index, counts[list2[i]])
      
      for count in counts:
        if counts[count] == min_index and count in restaurants_1 and count in restaurants_2:

          common_restaurants.append(count)
      
      return common_restaurants
# @lc code=end
