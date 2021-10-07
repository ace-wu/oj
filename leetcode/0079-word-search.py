class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        m = len(board)
        n = len(board[0])

        if m * n < l:
            return False

        def search(i, x, y):
            if i >= l:
                return True
            if not (0 <= x < m and 0 <= y < n):
                return False
            c = board[x][y]
            if word[i] != c:
                return False
            board[x][y] = '#'
            result = (
                search(i+1, x+1, y) or
                search(i+1, x-1, y) or
                search(i+1, x, y+1) or
                search(i+1, x, y-1)
            )
            board[x][y] = c
            return result

        for x in range(m):
            for y in range(n):
                if search(0, x, y):
                    return True
        return False


## TC: O(m*n*3^l)
## SC: O(l)
