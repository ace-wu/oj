from functools import cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def is_palindrome(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and is_palindrome(i+1, j-1)

        def iter_partitions(j):
            if j < 0:
                yield []
                return
            for i in range(j+1):
                if is_palindrome(i, j):
                    for part in iter_partitions(i-1):
                        part.append(s[i:j+1])
                        yield part

        return list(iter_partitions(len(s)-1))
