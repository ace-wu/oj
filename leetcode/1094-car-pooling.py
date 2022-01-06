from collections import defaultdict


class Solution:
    ## TC: O(n*log(n))
    ## SC: O(n)
    ## where n is len(trips)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capa_changes = defaultdict(int)
        for n, from_pos, to_pos in trips:
            capa_changes[from_pos] -= n
            capa_changes[to_pos] += n
        for pos, change in sorted(capa_changes.items()):
            capacity += change
            if capacity < 0:
                return False
        return True

    ## TC: O(n)
    ## SC: O(N)
    ## where n is len(trips), N is the max value of from_pos and to_pos
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capa_changes = [0] * 1001
        for n, from_pos, to_pos in trips:
            capa_changes[from_pos] -= n
            capa_changes[to_pos] += n
        for change in capa_changes:
            capacity += change
            if capacity < 0:
                return False
        return True
