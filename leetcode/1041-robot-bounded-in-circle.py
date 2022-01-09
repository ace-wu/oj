class Solution:
    # repeat 4 times
    ## TC: O(n)
    ## SC: O(1)
    def isRobotBounded(self, instructions: str) -> bool:
        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        x, y, d = 0, 0, 0
        for i in range(4):
            for inst in instructions:
                if inst == 'R':
                    d = (d + 1) % 4
                elif inst == 'L':
                    d = (d - 1) % 4
                elif inst == 'G':
                    dx, dy = DIR[d]
                    x += dx
                    y += dy
            if x == 0 and y == 0:
                return True
        return False

    # reduced method
    ## TC: O(n)
    ## SC: O(1)
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, -1
        for inst in instructions:
            if inst == 'R':
                dx, dy = -dy, dx
            elif inst == 'L':
                dx, dy = dy, -dx
            elif inst == 'G':
                x += dx
                y += dy
        return (x, y) == (0, 0) or (dx, dy) != (0, -1)
