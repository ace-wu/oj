from math import isqrt


class Solution:
    win = [False]

    # Bottom-up DP
    ## TC: O(n^1.5)
    ## SC: O(n)
    def winnerSquareGame(self, n: int) -> bool:
        if n >= len(self.win):
            for k in range(len(self.win), n + 1):
                i = 1
                while i * i <= k:
                    if not self.win[k - i * i]:
                        self.win.append(True)
                        break
                    i += 1
                else:
                    self.win.append(False)
        return self.win[n]


    # Bottom-up DP with isqrt
    ## TC: O(n^1.5)
    ## SC: O(n)
    def winnerSquareGame(self, n: int) -> bool:
        if n >= len(self.win):
            for k in range(len(self.win), n + 1):
                self.win.append(not all(self.win[k - i * i] for i in range(isqrt(k), 0, -1)))
        return self.win[n]
