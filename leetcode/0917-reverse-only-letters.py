class Solution:

    def reverseOnlyLetters_linear_space(self, s: str) -> str:
        def iter_reversed(s):
            is_letter = lambda c: 'a' <= c <= 'z' or 'A' <= c <= 'Z'
            stack = []
            for c in s:
                if is_letter(c):
                    stack.append(c)
            for c in s:
                yield stack.pop() if is_letter(c) else c
        return ''.join(iter_reversed(s))

    def reverseOnlyLetters(self, s: str) -> str:
        def iter_reversed(s):
            is_letter = lambda c: 'a' <= c <= 'z' or 'A' <= c <= 'Z'
            p = len(s) - 1
            for c in s:
                if is_letter(c):
                    while not is_letter(s[p]):
                        p -= 1
                    yield s[p]
                    p -= 1
                else:
                    yield c
        return ''.join(iter_reversed(s))


## TC: O(n)
## SC: O(1) extra space, O(n) output space

s = Solution()
print(s.reverseOnlyLetters('a-bC-dEf-ghIj'))
