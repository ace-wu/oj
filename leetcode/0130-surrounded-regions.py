class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def iter_boarder_pos():
            for x in range(m):
                yield x, 0
                yield x, n - 1
            for y in range(1, n):
                yield 0, y
                yield m - 1, y

        stack = [(x, y) for x, y in iter_boarder_pos() if board[x][y] == 'O']
        while stack:
            x, y = stack.pop()
            board[x][y] = '#'
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x+dx < m and 0 <= y+dy < n and board[x+dx][y+dy] == 'O':
                    stack.append((x+dx, y+dy))
        for x in range(m):
            for y in range(n):
                board[x][y] = 'O' if board[x][y] == '#' else 'X'


## TC: O(m*n)
## SC: O(m*n)
