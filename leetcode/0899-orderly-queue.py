class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # counting sort
        if k != 1:
            offset = ord('a')
            counter = [0] * 26
            for c in s:
                counter[ord(c) - offset] += 1
            return ''.join(chr(i + offset) for i, count in enumerate(counter) for _ in range(count))

        # min. string rotation
        length = len(s)
        p, q = 0, 1
        while p < length and q < length:
            for i in range(length):
                if s[(p + i) % length] > s[(q + i) % length]:
                    p += i + 1
                    break
                if s[(p + i) % length] < s[(q + i) % length]:
                    q += i + 1
                    break
            else:
                break
            if p == q:
                q += 1
        m = min(p, q) % length
        return s[m:] + s[:m]


## TC: O(n + |alphabet|)
## SC: O(|alphabet|)

s = Solution()
print(s.orderlyQueue('cba', 1))
print(s.orderlyQueue('cba', 2))
print(s.orderlyQueue('cbacbaabbb', 1))
print(s.orderlyQueue('cbacbaabbb', 2))
print(s.orderlyQueue('aaa', 1))
