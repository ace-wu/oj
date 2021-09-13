from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_counts = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        counter = Counter(text)
        return min(counter.get(c, 0) // count for c, count in balloon_counts.items())


# TC: O(n)
# SC: O(n)

s = Solution()
print(s.maxNumberOfBalloons('loonbalxballpoon'))
