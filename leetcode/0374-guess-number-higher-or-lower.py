class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 0, n
        while True:
            pick = (lower + upper) // 2
            result = guess(pick)
            if result == 0:
                return pick
            elif result > 0:
                lower = pick + 1
            else:
                upper = pick - 1


## TC: O(log(n))
## SC: O(1)
