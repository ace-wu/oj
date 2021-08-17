from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sums = [[0] * (n + 1)]
        for i in range(m):
            self.sums.append([0])
            for j in range(n):
                self.sums[i+1].append((
                    matrix[i][j]
                    + self.sums[i][j+1]
                    + self.sums[i+1][j]
                    - self.sums[i][j]
                ))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sums[row2+1][col2+1]
            - self.sums[row1][col2+1]
            - self.sums[row2+1][col1]
            + self.sums[row1][col1]
        )


## TC: build: O(n^2), query: O(1)
## SC: O(n^2)

nums = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
])

print(nums.sumRegion(2, 1, 4, 3))
print(nums.sumRegion(1, 1, 2, 2))
print(nums.sumRegion(1, 2, 2, 4))
