import collections


class Solution:
    ## TC: O(N)
    ## SC: O(N)
    ## tags: bitmask
    def wonderfulSubstrings(self, word: str) -> int:
        mask_map = {chr(ord('a') + i): 1 << i for i in range(10)}
        mask_count = collections.defaultdict(int)  # prefix_mask -> count
        prefix_mask = 0
        count = 0
        for c in word:
            prefix_mask ^= mask_map[c]
            count += mask_count[prefix_mask]
            for mask in mask_map.values():
                count += mask_count[prefix_mask ^ mask]
            if prefix_mask == 0 or (prefix_mask & (prefix_mask - 1)) == 0:
                count += 1
            mask_count[prefix_mask] += 1
        return count


s = Solution()
s.wonderfulSubstrings('aba')
s.wonderfulSubstrings('aabb')
