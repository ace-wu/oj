class Solution:
    ## TC: O(n)
    ## SC: O(1)
    ## tags: greedy
    def jump(self, nums: list[int]) -> int:
        step, farest, next_farest = 0, 0, 0
        for i, j in enumerate(nums):
            if i > farest:
                step += 1
                farest = next_farest
            next_farest = max(i + j, next_farest)
        return step
