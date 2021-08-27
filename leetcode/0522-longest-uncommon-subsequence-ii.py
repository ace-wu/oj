from typing import List
from collections import defaultdict

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub_sequence(a, b):
            ia, ib = 0, 0
            if len(a) > len(b):
                return False
            while ib < len(b) and ia < len(a):
                if a[ia] == b[ib]:
                    ia += 1
                ib += 1
            return ia == len(a)

        # length -> string -> count
        counts = defaultdict(lambda: defaultdict(int))
        for s in strs:
            counts[len(s)][s] += 1
        seen = set()
        for length in sorted(counts.keys(), reverse=True):
            skip = set()
            for s, count in counts[length].items():
                if count > 1:
                    continue
                if any(is_sub_sequence(s, seen_s) for seen_s in seen):
                    skip.add(s)
                    continue
                return len(s)
            seen.update(counts[length].keys())
            seen -= skip
        return -1


## TC: O(n^2)
## SC: O(n) extra space

s = Solution()
print(s.findLUSlength(['aba','cdc','eae']))
print(s.findLUSlength(['aaa','aaa','aa']))
print(s.findLUSlength(['aabbcc', 'aabbcc','bc','bcc']))
