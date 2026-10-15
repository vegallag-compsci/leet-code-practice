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
        dicti = {}
        last_row = 0
        last_col = 0

        # add all chars & coords (row,col) to dictionary 'dicti'
        for row in range(len(board)): 
            for col in range(len(board[0])):
                curr_letter = board[row][col]
                if curr_letter in word:
                    dicti[curr_letter] = (row, col)

        # check every char's placement and make sure it's touching the last
        # row and col (abs() == 1)
        for i, char in enumerate(word):
            row, col = dicti[char]
            # Debug
            print(f"({char}) at {row, col}, {abs((row + col) - (last_row + last_col))}")
            if i == 0:
                last_row = row
                last_col = col
                continue
            if abs((row + col) - (last_row + last_col)) == 1 and not i == 0:
                last_row = row
                last_col = col
                continue
            elif not abs((row + col) - (last_row + last_col)) == 1:
                return False

        return True

        


sol = Solution()
table1 = [["A", "B", "C"],
          ["D", "E", "F"],
          ["G", "H", "I"]]
table2 = [["A", "B", "C", "D"],
          ["E", "F", "G", "H"],
          ["I", "J", "K", "L"]]
# table 1 (true: ADGHIFCBA)
# table 2 (false: ADEFH)
# table 2 (true: ABFGH)
# table 2 (false: ABFJG)
result = sol.exist(table1, "ADEFH")
print("Result:", result)