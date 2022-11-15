class MyQueue:

    def __init__(self):
        self.stack = []
        self.length = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length += 1  
        
    def pop(self) -> int:
        stack2 = []
        for i in range(self.length):
            stack2.append(self.stack.pop())
        res = stack2.pop()
        self.length -= 1
        for i in range(self.length):
            self.stack.append(stack2.pop())
        return res

    def peek(self) -> int:
        stack2 = self.stack.copy()
        for i in range(self.length-1):
            stack2.pop()
        return stack2.pop()
        
    def empty(self) -> bool:
        if self.length == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()