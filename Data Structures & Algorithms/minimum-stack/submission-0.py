class MinStack:

    def __init__(self):
        self.stack = []
        self.minima = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minima) > 0:
            self.minima.append(min(val, self.minima[-1]))
        else:
            self.minima.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minima.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minima[-1]
