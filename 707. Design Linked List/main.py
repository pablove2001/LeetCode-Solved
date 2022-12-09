class MyLinkedList:

    def __init__(self):
        self.l = []

    def get(self, index: int) -> int:
        if 0 <= index < len(self.l):
            return self.l[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.l = [val] + self.l 

    def addAtTail(self, val: int) -> None:
        self.l.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.l) or index < 0:
            return
        self.l = self.l[0:index] + [val] + self.l[index:]

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.l):
            self.l.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)