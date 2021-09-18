class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inf = float('inf')
        n = len(matrix)
        curr_sum = [0] * n
        prev_sum = [0] * n
        get_value = lambda row, i: row[i] if 0 <= i < n else inf
        for row in matrix:
            prev_sum, curr_sum = curr_sum, prev_sum
            for i in range(n):
                curr_sum[i] = row[i] + min(get_value(prev_sum, i-1), get_value(prev_sum, i), get_value(prev_sum, i+1))
        return min(curr_sum)


## TC: O(n^2)
## SC: O(n)
