class Solution:
    def longestPalindrome(self, text: str) -> str:
        length = len(text)
        if length == 1:
            return text
        answer = (0, 0)
        table = [[True] * length for _ in range(length)]
        for l in range(2, length + 1):
            for start in range(length - l + 1):
                end = start + l - 1
                table[start][end] = table[start+1][end-1] and text[start] == text[end]
                if table[start][end]:
                    answer = start, end
        return text[answer[0]:answer[1]+1]


## TC: O(n^2), can be reduced to O(n) by Manacher's algorithm
## SC: O(n^2)
