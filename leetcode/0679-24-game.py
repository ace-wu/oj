from typing import List
from itertools import permutations

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return -10e-10 <= cards[0] - 24 <= 10e-10
        for a, b, *tail in permutations(cards):
            for c in {a+b, a-b, a*b, b and a/b}:
                if self.judgePoint24([c] + tail):
                    return True
        return False


s = Solution()
print(s.judgePoint24([4,1,8,7]))
print(s.judgePoint24([1,2,1,2]))
print(s.judgePoint24([3,3,8,8]))
