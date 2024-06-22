class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        size_list = []
        size = 1
        for i in nums + [1]:
            if i & 1 == 0:
                size += 1
            else:
                size_list.append(size)
                size = 1
        if k == 0:
            return sum(size_list)
        return sum(a * b for a, b in zip(size_list[:-k], size_list[k:]))
