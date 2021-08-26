import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c)) + 1
        while a <= b:
            c_ = a**2 + b**2
            if c_ == c:
                return True
            elif c_ < c:
                a += 1
            else: # c_ > c:
                b -= 1
        return False


## TC: O(n^0.5)
## SC: O(1)

s = Solution()
print(s.judgeSquareSum(1))
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(4))
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(2**31-1))
