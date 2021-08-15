from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        length = len(boxes)

        last_seen = {}
        next_index = [0] * length
        for i in range(length - 1, -1, -1):
            k = boxes[i]
            next_index[i] = last_seen.get(k, length + 1)
            last_seen[k] = i

        table = [[None] * length for _ in range(length)]
        return self.max_score(0, length-1, boxes, table, next_index)

    def max_score(self, i, j, boxes, table, next_index):
        if i > j:
            return 0
        if i == j:
            return 1
        if table[i][j]:
            return table[i][j]
        accum_score = 0
        selected = 1
        result = 0
        cursor = i
        while cursor <= j:
            #result = max(result, accum_score + selected**2 + self.max_score(cursor+1, j, boxes, table, next_index))
            new_result = accum_score + selected**2 + self.max_score(cursor+1, j, boxes, table, next_index)
            if new_result > result:
                solution = (selected, accum_score, (cursor+1, j))
                result = new_result
            next_cursor = next_index[cursor]
            if next_cursor > j:
                break
            selected += 1
            accum_score += self.max_score(cursor+1, next_cursor-1, boxes, table, next_index)
            cursor = next_cursor
        print(f'({i}, {j}): {solution}')
        table[i][j] = result
        return result



s = Solution()
print(s.removeBoxes([1,2,2,1,1,1,2,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,2,2,2,2,1,2,1,1,2,2,1,2,1,2,2,2,2,2,1,2,1,2,2,1,1,1,2,2,1,2,1,2,2,1,2,1,1,1,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,2,2,1]))
#print(s.removeBoxes([8,1,2,10,8,5,1,10,8,4]))
#print(s.removeBoxes([1,3,2,2,2,3,4,3,1]))
#print(s.removeBoxes([1,1,1]))
#print(s.removeBoxes([1]))

#[1,3,2,2,2,3,4,3,1]
#
#[1,  3,2,2,2,3,4,3,1]
#[1,  3,2,2,2,3,4,3,  1]
#
#[3,2,2,2,3,4,3,1]
#
#[3,  2,2,2,3,4,3,1]
#
#[3,  2,2,2,  3,  4,3,1]
#
#[3,  2,2,2,  3,  4,  3,  1]
#
#1 22 33 44 55 1 66 44 33 22 1 7 1 7 1
