class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        m = len(matrix)
        n = len(matrix[0])
        is_available = lambda i, j: 0 <= i < m and 0 <= j < n and matrix[i][j] is not None

        result = []
        i, j, d = 0, 0, 0
        while True:
            result.append(matrix[i][j])
            matrix[i][j] = None
            if not is_available(i + di[d], j + dj[d]):
                d = (d + 1) % 4
                if not is_available(i + di[d], j + dj[d]):
                    return result
            i += di[d]
            j += dj[d]
        return result


## TC: O(m+n)
## SC: O(m+n)  (inplace or extra space)
