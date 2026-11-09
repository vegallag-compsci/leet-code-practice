"""
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""

from collections import Counter

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize starting length of w1, w2
        m, n = len(word1), len(word2)

        return 1


sol = Solution()
result = sol.minDistance(word1 = "horse", word2 = "ros")
print("Result:", result)