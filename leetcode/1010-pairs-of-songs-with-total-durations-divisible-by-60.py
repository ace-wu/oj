from collections import Counter, defaultdict


class Solution:
    ## TC: O(n)
    ## SC: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter(t % 60 for t in time)
        pairs = 0
        pairs += counter.get(0, 0) * (counter.get(0, 0) - 1) // 2
        pairs += counter.get(30, 0) * (counter.get(30, 0) - 1) // 2
        for i in range(1, 30):
            pairs += counter.get(i, 0) * counter.get(60 - i, 0)
        return pairs

    ## TC: O(n)
    ## SC: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        counter = defaultdict(int)
        for t in time:
            t %= 60
            pairs += counter.get((60 - t) % 60, 0)
            counter[t] += 1
        return pairs
