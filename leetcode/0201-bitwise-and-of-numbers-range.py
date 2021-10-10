class Solution:
    def rangeBitwiseAnd_scan_msb(self, left: int, right: int) -> int:
        msb = 1
        while msb << 1 <= right:
            msb <<= 1
        common_bits = 0
        while msb:
            if right >= msb:
                if left < msb:
                    break
                common_bits |= msb
                left -= msb
                right -= msb
            msb >>= 1
        return common_bits

    def rangeBitwiseAnd_remove_lsb(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return right << shift

    def rangeBitwiseAnd_remove_lsb2(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1
        return right


# TC: O(log(n))
# SC: O(1)

s = Solution()
assert 0 == s.rangeBitwiseAnd(1, 2147483647)
assert 4 == s.rangeBitwiseAnd(5, 7)
assert 5 == s.rangeBitwiseAnd(5, 5)
assert 3 == s.rangeBitwiseAnd(3, 3)
