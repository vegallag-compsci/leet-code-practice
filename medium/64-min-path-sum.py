"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

from collections import Counter

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # e
        print('e')


sol = Solution()
result = sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]) # -> 7
print("Result:", result)