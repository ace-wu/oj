from typing import List
from collections import defaultdict


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        counter = defaultdict(lambda: defaultdict(int))
        for i, (x, y) in enumerate(moves):
            player = 'A' if i & 1 == 0 else 'B'
            counter[player][f'x{x}'] += 1
            counter[player][f'y{y}'] += 1
            if x == y:
                counter[player]['diag1'] += 1
            if x + y == 2:
                counter[player]['diag2'] += 1
        if any(v >= 3 for v in counter['A'].values()):
            return 'A'
        if any(v >= 3 for v in counter['B'].values()):
            return 'B'
        if len(moves) == 3 * 3:
            return 'Draw'
        return 'Pending'


## TC: O(n*n)
## SC: O(n)

s = Solution()
print(s.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(s.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(s.tictactoe([[0,0],[1,1]]))
