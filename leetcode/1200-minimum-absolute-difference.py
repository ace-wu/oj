class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(a - b for a, b in zip(arr[1:], arr))
        return [[b, a] for a, b in zip(arr[1:], arr) if a - b == min_diff]


## TC: O(n)
## SC: O(n)
