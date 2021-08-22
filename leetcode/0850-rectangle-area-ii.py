from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        x_values = set()
        y_values = set()
        for x1, y1, x2, y2 in rectangles:
            x_values.add((x1, y1, y2, 1)) # left
            x_values.add((x2, y1, y2, -1)) # right
            y_values.add(y1)
            y_values.add(y2)

        x_values = list(sorted(x_values))
        y_values = list(sorted(y_values))
        y_indices = {y: i for i, y in enumerate(y_values)}
        y_delta = [y1 - y0 for y0, y1 in zip(y_values, y_values[1:])]
        y_layers = [0] * len(y_delta)

        total_area = 0
        prev_x = 0
        for x, y1, y2, layer_change in x_values:
            total_area += (x - prev_x) * sum(delta for layer, delta in zip(y_layers, y_delta) if layer)
            prev_x = x
            for yi in range(y_indices[y1], y_indices[y2]):
                y_layers[yi] += layer_change

        return total_area % (10 ** 9 + 7)


## TC: O(n^2)
## SC: O(n)

s = Solution()
print(s.rectangleArea([
    [0,0,2,2],
    [1,0,2,3],
    [1,0,3,1],
]))
print(s.rectangleArea([
    [0,0,1000000000,1000000000],
]))
