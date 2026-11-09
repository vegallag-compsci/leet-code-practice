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
        # Initialize table of size (m+1)x(n+1)
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill base cases (first row/col)
        # string length i -> empty string (takes i deletions)
        for i in range(m + 1):
            dp[i][0] = i

        # empty string -> string length j (takes j insertions)
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill rest of grid
        # Loop through each cell
        # If chars match: dp[i][j] = dp[i-1][j-1]
        # If dont match: dp[i][j] = 1 + min(delete, insert, substitute)
        

        # Return result (bottom-right corner of table)
        return dp[m][n]



sol = Solution()
result = sol.minDistance(word1 = "horse", word2 = "ros")
print("Result:", result)