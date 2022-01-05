class Solution:
    ## TC: O(log(n))
    ## SC: O(1)
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bit = 1
        while bit <= n:
            bit <<= 1
        return n ^ (bit - 1)
