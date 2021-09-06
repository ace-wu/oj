from typing import List
from itertools import chain


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration, max_key = 0, ''
        for press, release, key in zip(chain([0], releaseTimes), releaseTimes, keysPressed):
            duration = release - press
            if duration > max_duration or (duration == max_duration and key > max_key):
                max_duration, max_key = duration, key
        return max_key


## TC: O(n)
## SC: O(1)

s = Solution()
print(s.slowestKey([9,29,49,50], 'cbcd'))
print(s.slowestKey([12,23,36,46,62], 'spuda'))
