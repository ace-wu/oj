import functools


class Solution:
    ## TC: O(n^2 * m)
    ## SC: O(n * m)
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_size = len(ring)
        ring = ring * 2
        inf = float('inf')

        @functools.cache
        def min_steps(ring_i, key_i):
            if key_i == len(key):
                return 0
            key_c = key[key_i]
            result = inf
            for i, c in enumerate(ring[ring_i : ring_i + ring_size]):
                if c != key_c:
                    continue
                steps = min(i, ring_size - i) + min_steps(
                    (ring_i + i) % ring_size, key_i + 1
                )
                result = min(steps, result)
            return result

        return min_steps(0, 0) + len(key)
