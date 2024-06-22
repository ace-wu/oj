class Solution:
    ## TC: O(nlogn)
    ## SC: O(n)
    def heightChecker(self, heights: list[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))

    ## TC: O(n)
    ## SC: O(n)
    def heightChecker_counting_sort(self, heights: list[int]) -> int:
        MAX_NUMBER = 100
        def iter_sorted(nums):
            counter = [0] * (MAX_NUMBER + 1)
            for k in nums:
                counter[k] += 1
            for i, c in enumerate(counter):
                for _ in range(c):
                    yield i
        return sum(a != b for a, b in zip(heights, iter_sorted(heights)))
