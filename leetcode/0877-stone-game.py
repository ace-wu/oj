from typing import List


class Solution:
    def stoneGame_math(self, piles: List[int]) -> bool:
        # color stones into black and white stone by parity
        # if one color has larger count, always choose that color
        return True

    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        max_map = [[0] * length for n in range(length)]
        for k in range(0, length):
            for i in range(length - k):
                sign = 1 if (length - k) & 1 else -1
                j = i + k
                if i == j:
                    max_map[i][j] = piles[i] * sign
                elif sign == 1:
                    max_map[i][j] = max(max_map[i+1][j] + piles[i], max_map[i][j-1] + piles[j])
                else:
                    max_map[i][j] = min(max_map[i+1][j] - piles[i], max_map[i][j-1] - piles[j])
        return max_map[0][length-1] > 0


s = Solution()
print(s.stoneGame([5,3,4,5]))
print(s.stoneGame([1,2,10,2,2,4,4]))
