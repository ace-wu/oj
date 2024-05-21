class Solution:
    ## TC: O(2^n)
    ## SC: O(n*2^n) for output space, O(n) for backtracking space
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def iter_subsets(subset, pos):
            if pos >= len(nums):
                yield subset
                return
            yield from iter_subsets(subset, pos + 1)
            subset.append(nums[pos])
            yield from iter_subsets(subset, pos + 1)
            subset.pop()

        return [list(subset) for subset in iter_subsets([], 0)]
