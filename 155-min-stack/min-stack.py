class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float(("inf"))
        
    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.mini = val
        else:
            self.mini = min(self.mini,val)

        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()