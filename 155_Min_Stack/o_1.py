class MinStack:

    def __init__(self):
        self.min = []
        self.inventory = []

    def push(self, val: int) -> None:
        self.inventory.append(val)
        self.min.append(min(val, self.min[-1]) if self.min else val)

    def pop(self) -> None:
        del self.min[-1]
        return self.inventory.pop()

    def top(self) -> int:
        return self.inventory[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

