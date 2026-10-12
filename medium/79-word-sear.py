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
        letters_found = ""
        found = 0
        last_row = 0
        last_col = 0

        for i, row in enumerate(board):
            for char in range(len(row)):
                row_num = i
                row_index = char
                row_letter = row[char]

                if row_letter in word and row_letter not in letters_found:
                    if found == 0:
                        letters_found += row_letter
                        found += 1
                        last_row = row_num
                        last_col = row_index
                        print('Found: '+str(found), 'Last_Row: '+str(last_row), 'Last_Col: '+str(last_col))
                    else:
                        if row_num == last_row + 1 or last_row - 1:
                            if  row_index == last_col + 1 or last_col - 1:
                                letters_found += row_letter
                                found += 1
                                last_row = row_num
                                last_col = row_index
                                print('Found: '+str(found), 'Last_Row: '+str(last_row), 'Last_Col: '+str(last_col))        
        
        if found == len(word):
            return True
        else:
            return False

        


sol = Solution()
result = sol.exist([["A", "B", "C"],
                    ["D", "E", "F"],
                    ["G", "H", "I"]], "ADGHI")
print("Result:", result)