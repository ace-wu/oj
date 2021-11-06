class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        for n in nums:
            r1 = ~r2 & (r1 ^ n)
            r2 = ~r1 & (r2 ^ n)
        return r1


# count % 3 == 0: (r1, r2) = (0, 0)
# count % 3 == 1: (r1, r2) = (1, 0)
# count % 3 == 2: (r1, r2) = (0, 2)
#
# r1 r2  n  r1' r2'
#
#  0  0  0    0  0
#  1  0  0    1  0
#  0  1  0    0  1
#  1  1  0    -  -
#
#  0  0  1    1  0
#  1  0  1    0  1
#  0  1  1    0  0
#  1  1  1    -  -


## TC: O(n)
## SC: O(1)
