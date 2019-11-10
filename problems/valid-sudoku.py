# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board):
        row_dict = {i: [] for i in range(9)}
        col_dict = {i: [] for i in range(9)}
        window_dict = {(i+1): [] for i in range(9)}
        
        # create a copy of the board filled with area codes 1-9 
        mat = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if i < 3:
                    if j < 3:
                        mat[i][j] = 1
                    if 3 <= j < 6:
                        mat[i][j] = 2
                    if 6 <= j < 9:
                        mat[i][j] = 3
                elif 3 <= i < 6:
                    if j < 3:
                        mat[i][j] = 4
                    if 3 <= j < 6:
                        mat[i][j] = 5
                    if 6 <= j < 9:
                        mat[i][j] = 6
                else:
                    if j < 3:
                        mat[i][j] = 7
                    if 3 <= j < 6:
                        mat[i][j] = 8
                    if 6 <= j < 9:
                        mat[i][j] = 9
           
        for i in range(9):
            for j in range(9):
                elem = board[i][j] 
                if elem != '.':
                    # check if elem is already in either the i-th row or j-th column 
                    if elem in row_dict[i] or elem in col_dict[j]:
                        return False
                    
                    # check if elem is already in the k-th 3x3 sub-box 
                    k = mat[i][j] 
                    if elem in window_dict[k]:
                        return False
                    
                    # if element hasn't appeard before, save it 
                    row_dict[i].append(elem)
                    col_dict[j].append(elem)
                    window_dict[k].append(elem)
                    
        return True

                    
