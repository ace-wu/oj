from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_chars = sorted(((count, c) for c, count in Counter(s).items()), reverse=True)
        return ''.join(c * count for count, c in sorted_chars)


## TC: O(n + k*log(k))
## SC: O(n) for output space, O(k) for extra space
## where n = len(n), k is the size of the alphabet (26 in this case)
