class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        
    def push(self, val: int) -> None:
        if self.mini:
            self.mini.append(min(val, self.mini[-1]))
        else:
            self.mini.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()