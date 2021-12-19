class Solution:
    def decodeString(self, s: str) -> str:
        def iter_strings(s, start, end):
            while start < end:
                if s[start] == ']':
                    return start + 1
                elif 'a' <= s[start] <= 'z':
                    yield s[start]
                    start += 1
                elif '0' <= s[start] <= '9':
                    digit_end = s.index('[', start)
                    for i in range(int(s[start:digit_end])):
                        start = yield from iter_strings(s, digit_end + 1, end)
        return ''.join(iter_strings(s, 0, len(s)))


## TC: O(m)
## SC: O(m)
## where m is the length of the output string
