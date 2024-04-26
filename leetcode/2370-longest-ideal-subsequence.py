class Solution:
    ## TC: O(n^2) TLE
    ## SC: O(n)
    def longestIdealString_TLE(self, s: str, k: int) -> int:
        lis_with_tail = []
        for i in range(len(s)):
            ord_tail = ord(s[i])
            current_lis = 1
            for j in range(i):
                if abs(ord(s[j]) - ord_tail) <= k:
                    current_lis = max(current_lis, lis_with_tail[j] + 1)
            lis_with_tail.append(current_lis)
        return max(lis_with_tail)

    ## TC: O(min(k, 26) * n) = O(n)
    ## SC: O(1)
    def longestIdealString(self, s: str, k: int) -> int:
        # idx: 'a'=0, 'b'=1, ..., and so on.
        lis = [0] * 26  # idx -> lis ends with idx
        for i in range(len(s)):
            tail = ord(s[i]) - ord('a')
            begin = max(tail - k, 0)
            end = min(tail + k + 1, len(lis))
            lis_with_tail = max(lis[begin:end] or [0]) + 1
            lis[tail] = max(lis[tail], lis_with_tail)
        return max(lis)
