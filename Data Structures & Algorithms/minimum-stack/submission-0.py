class MinStack:

    def __init__(self):
        self.items = []
        self.tracker = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.tracker or val <= self.tracker[-1]:
            self.tracker.append(val)

    def pop(self) -> None:
       val = self.items.pop()
       if val == self.tracker[-1]:
            self.tracker.pop()
    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.tracker[-1]
