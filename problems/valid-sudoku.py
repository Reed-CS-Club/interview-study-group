# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board):
        row_dict = {i: [] for i in range(9)}
        col_dict = {i: [] for i in range(9)}
        window_dict = {i: [] for i in range(9)}
           
        for i in range(9):
            for j in range(9):
                elem = board[i][j] 
                if elem != '.':
                    # check if elem is already in either the i-th row or j-th column 
                    if elem in row_dict[i] or elem in col_dict[j]:
                        return False
                    
                    # get sub-box number
                    k = (i // 3 ) * 3 + j // 3
                    if elem in window_dict[k]:
                        return False
                    
                    # if element hasn't appeard before, save it 
                    row_dict[i].append(elem)
                    col_dict[j].append(elem)
                    window_dict[k].append(elem)
                    
        return True
        