from collections import defaultdict, deque


class Solution:
    # TC: O(n)
    # SC: O(n)
    def minJumps(self, arr: List[int]) -> int:
        last_idx = len(arr) - 1
        jump_links = defaultdict(list)
        for idx, val in enumerate(arr):
            jump_links[val].append(idx)
        seen_idx = set([0])
        seen_val = set()
        queue = deque([(0, 0)])
        while queue:
            idx, steps = queue.popleft()
            if idx == last_idx:
                return steps
            if arr[idx] not in seen_val:
                for next_idx in jump_links[arr[idx]]:
                    if next_idx not in seen_idx:
                        seen_idx.add(next_idx)
                        queue.append((next_idx, steps + 1))
            for next_idx in [idx - 1, idx + 1]:
                if next_idx not in seen_idx and 0 <= next_idx <= last_idx:
                    seen_idx.add(next_idx)
                    queue.append((next_idx, steps + 1))
            seen_val.add(arr[idx])
