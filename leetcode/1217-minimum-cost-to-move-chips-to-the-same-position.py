class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counter = [0, 0]
        for pos in position:
            counter[pos % 2] += 1
        return min(counter)


## TC: O(n)
## SC: O(1)
