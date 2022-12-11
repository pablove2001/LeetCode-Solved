class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = []
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if len(self.arr) < self.k:
            self.arr.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.arr:
            self.arr.pop(0)
            return True
        return False

    def Front(self) -> int:
        if self.arr:
            return self.arr[0]
        return -1        
        
    def Rear(self) -> int:
        if self.arr:
            return self.arr[-1]
        return -1        

    def isEmpty(self) -> bool:
        return not self.arr       

    def isFull(self) -> bool:
        return len(self.arr) == self.k
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()