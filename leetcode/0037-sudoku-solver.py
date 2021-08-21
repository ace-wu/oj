from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        get_bit = lambda flag, n: (flag >> n) & 1
        set_bit = lambda flag, n: flag | (1 << n)
        unset_bit = lambda flag, n: flag & ~(1 << n)
        kth_box = lambda r, c: (r // 3) * 3 + (c // 3)

        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        empty_cells = []

        def update_flags(op, r, c, b, number):
            rows[r] = op(rows[r], number)
            cols[c] = op(cols[c], number)
            boxes[b] = op(boxes[b], number)

        def is_available(r, c, b, number):
            return not (get_bit(rows[r], number) or get_bit(cols[c], number) or get_bit(boxes[b], number))

        for r in range(9):
            for c in range(9):
                b = kth_box(r, c)
                if board[r][c] == '.':
                    empty_cells.append((r, c, b))
                else:
                    number = int(board[r][c])
                    update_flags(set_bit, r, c, b, number)

        def is_solved(kth):
            if kth == len(empty_cells):
                return True
            r, c, b = empty_cells[kth]
            for number in range(1, 10):
                if is_available(r, c, b, number):
                    update_flags(set_bit, r, c, b, number)
                    board[r][c] = str(number)
                    if is_solved(kth + 1):
                        return True
                    update_flags(unset_bit, r, c, b, number)
            return False

        assert is_solved(0)
        #for row in board:
        #    print(''.join(row))


## TC: O(n^k)
## SC: O(n+k)
## where n == 9 and k == #empty_cells

s = Solution()
s.solveSudoku([
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9'],
])
