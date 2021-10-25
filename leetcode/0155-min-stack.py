class MinStack:

    def __init__(self):
        self.min_stack = [float('inf')]
        self.val_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(min(self.min_stack[-1], val))
        self.val_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.val_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


## TC: O(1)
## SC: O(n)
