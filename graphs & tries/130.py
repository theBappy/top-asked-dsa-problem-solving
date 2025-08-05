# Tc = O(n.m) [row.col of grid]
# Sc = O(1)
# Surrounded Regions
# Apple, Google
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0]) 

        # 1) (DFS) capture the un-surrounded region (O->T)
        def capture(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
                
        # 2) capture the surrounded region (O->X)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r, c)  

        # 3) un-capture un-surrounded region (T->O) and capture surrounded region (O->X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

