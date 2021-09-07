from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        length = len(trees)
        if length <= 3:
            return trees

        cprod = lambda x, y: x[0]*y[1] - x[1]*y[0]
        is_cw =  lambda x, y, z: cprod(x, y) + cprod(y, z) + cprod(z, x) <= 0
        is_ccw = lambda x, y, z: cprod(x, y) + cprod(y, z) + cprod(z, x) >= 0

        trees = sorted(trees)
        upper = trees[:2]
        lower = trees[:2]
        for i in range(2, len(trees)):
            x = trees[i]
            while len(upper) >= 2 and not is_cw(upper[-2], upper[-1], x):
                upper.pop()
            upper.append(x)
            while len(lower) >= 2 and not is_ccw(lower[-2], lower[-1], x):
                lower.pop()
            lower.append(x)
        return set(tuple(x) for x in upper + lower)


## TC: O(n*log(n))
## SC: O(n)

s = Solution()
print(s.outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))
print(s.outerTrees([[1,2],[2,2],[4,2]]))
