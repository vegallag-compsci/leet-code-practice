"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # isTouching() 
        total_rows = len(board)
        total_cols = len(board[0])
        prog = 0
        track = ""
        row_l, col_l = 0,0

        for row in range(rows):
            for col in range(cols):
                curr_letter = board[row][col]
                if curr_letter == word[prog]:
                    print(f"'{curr_letter}' is at {row, col}")
                    if row + 1 < len(total_rows):
                        if
                    if row - 1 >= 0:

                    if col + 1 < len(total_cols):

                    if col - 1 >= 0:


        if prog == word:
            return True
        else:
            return False

        


sol = Solution()
result = sol.exist([["A", "B", "C"],
                    ["D", "E", "F"],
                    ["G", "H", "I"]], "ADGHI")
print("Result:", result)