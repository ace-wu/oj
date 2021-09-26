from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # make sure rows/columns are either equal or complement to each other
        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] ^ board[i-1][j] ^ board[i][j-1] ^ board[i-1][j-1]:
                    return -1

        # make sure the number of each kind of rows/columns compliment are half-and-half
        possible_1_count = set([n//2, (n+1)//2])
        if sum(board[0]) not in possible_1_count:
            return -1
        if sum(board[i][0] for i in range(n)) not in possible_1_count:
            return -1

        row_parity_0 = sum(board[0][i] ^ (i&1) for i in range(n))
        col_parity_0 = sum(board[i][0] ^ (i&1) for i in range(n))
        row_parity_1 = n - row_parity_0
        col_parity_1 = n - col_parity_0
        if n & 1:
            rows_to_swap = row_parity_1 if row_parity_0 & 1 else row_parity_0
            cols_to_swap = col_parity_1 if col_parity_0 & 1 else col_parity_0
        else:
            rows_to_swap = min(row_parity_0, row_parity_1)
            cols_to_swap = min(col_parity_0, col_parity_1)
        return (rows_to_swap + cols_to_swap) // 2


## TC: O(n^2)
## SC: O(n)

s = Solution()
print(s.movesToChessboard([
    [0,1,1,0],
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
]))
print(s.movesToChessboard([
    [0,1],
    [1,0],
]))
print(s.movesToChessboard([
    [1,0],
    [1,0],
]))
print(s.movesToChessboard([
    [1,1,0],
    [0,0,1],
    [0,0,1],
]))
print(s.movesToChessboard([
    [1,0,0],
    [0,1,1],
    [1,0,0],
]))
print(s.movesToChessboard([
    [0,0,1,1],
    [1,1,0,0],
    [0,1,0,1],
    [1,0,1,0],
]))
