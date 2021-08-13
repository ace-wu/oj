from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return [[word for word in group] for group in groups.values()]


s = Solution()
print(s.groupAnagrams(['eat','tea','tan','ate','nat','bat']))
print(s.groupAnagrams(['']))
print(s.groupAnagrams([]))
