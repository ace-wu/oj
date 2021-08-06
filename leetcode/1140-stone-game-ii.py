from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        max_map = [[0] * length for n in range(length)]
        for i in range(length):
            for m in range(i+1):
                max_map[i, m] =
        pass

    def alice_max(self, piles, i, m):
