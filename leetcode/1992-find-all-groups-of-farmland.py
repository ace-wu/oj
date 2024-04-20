class Solution:
    ## TC: O(m * n)
    ## SC: O(1) using the input space, O(m * n) output space
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        m = len(land)
        n = len(land[0])

        def mark_farmland(land, r1, c1):
            r2, c2 = r1, c1
            while r2 + 1 < m and land[r2 + 1][c2] == 1:
                r2 += 1
            while c2 + 1 < n and land[r2][c2 + 1] == 1:
                c2 += 1
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    land[r][c] = -1
            return r1, c1, r2, c2

        coordinate_list = []
        for r in range(m):
            for c in range(n):
                if land[r][c] != 1:
                    continue
                coordinate_list.append(mark_farmland(land, r, c))
        return coordinate_list
