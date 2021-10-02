class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        m = len(text1)
        n = len(text2)
        curr_row = [0] * (m + 1)
        next_row = [0] * (m + 1)
        for j in range(n):
            for i in range(m):
                if text1[i] == text2[j]:
                    next_row[i+1] = curr_row[i] + 1
                else:
                    next_row[i+1] = max(curr_row[i+1], next_row[i])
            curr_row, next_row = next_row, curr_row
        return curr_row[-1]


## TC: O(m*n)
## SC: O(min(m, n))
