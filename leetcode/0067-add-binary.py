from itertools import zip_longest


class Solution:
    ## TC: O(n)
    ## SC: O(n)
    def addBinary(self, a: str, b: str) -> str:
        digits = []
        carry = '0'
        for ac, bc in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            if ac == bc:
                digits.append(carry)
                carry = ac
            else:
                digits.append('0' if carry == '1' else '1')
        if carry == '1':
            digits.append(carry)
        return ''.join(digits[::-1])

    ## TC: O(n)
    ## SC: O(n)
    def addBinary(self, a: str, b: str) -> str:
        digits = []
        carry = '0'
        ai, bi = len(a) - 1, len(b) - 1
        while ai >= 0 or bi >= 0 or carry == '1':
            ac = a[ai] if ai >= 0 else '0'
            bc = b[bi] if bi >= 0 else '0'
            if ac == bc:
                digits.append(carry)
                carry = ac
            else:
                digits.append('0' if carry == '1' else '1')
            ai, bi = ai - 1, bi - 1
        return ''.join(digits[::-1])
