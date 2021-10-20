class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


## TC: O(n) since python string is immutable
## SC: O(n)
