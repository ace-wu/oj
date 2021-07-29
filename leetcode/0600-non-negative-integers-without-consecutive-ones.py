class Solution:
    def findIntegers(self, n: int) -> int:
        f1, f2 = 1, 2
        count = 0
        n += 1
        while n:
            if n & 3 == 3:
                count = 0
            if n & 1:
                count += f1
            n >>= 1
            f1, f2 = f2, f1 + f2
        return count

    def check(self, n: int):
        count = 0
        for i in range(n + 1):
            count += 1
            while i >= 3:
                if i & 3 == 3:
                    count -= 1
                    break
                i >>= 1
        return count

s = Solution()
for k in range(10000):
    ans = s.findIntegers(k)
    check = s.check(k)
    print(f'{k}: {ans} {check}')
    if ans != check:
        print()
        break

#print(s.findIntegers(20))
#print(s.check(20))
