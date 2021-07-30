from typing import List

class Solution:
    def iteritems_in_row(self, board, n):
        for j in range(9):
            yield board[n][j]

    def iteritems_in_column(self, board, n):
        for i in range(9):
            yield board[i][n]

    def iteritems_in_block(self, board, n):
        i_offset = (n // 3) * 3
        j_offset = (n % 3) * 3
        for k in range(9):
            i = k // 3
            j = k % 3
            yield board[i + i_offset][j + j_offset]

    def is_nums_valid(self, num_iter):
        num_iter = list(num_iter)
        seen = set()
        for n in num_iter:
            if n == '.':
                continue
            if n in seen:
                return False
            seen.add(n)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            all(self.is_nums_valid(self.iteritems_in_row(board, n))    for n in range(9)) and
            all(self.is_nums_valid(self.iteritems_in_column(board, n)) for n in range(9)) and
            all(self.is_nums_valid(self.iteritems_in_block(board, n))  for n in range(9))
        )

s = Solution()

print(s.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))

print(s.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))
