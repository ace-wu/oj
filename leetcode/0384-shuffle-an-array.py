from random import randrange


class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        result = self.origin[:]
        n = len(result)
        temp = result[0]
        for i in range(n):
            j = randrange(i, n)
            result[i], result[j] = result[j], result[i]
        return result
