class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.arr)):
            if end <= self.arr[i][0]:
                if i == 0:
                    self.arr.insert(0, [start, end])
                    return True
                if self.arr[i-1][1] <= start:
                    self.arr.insert(i, [start, end])
                    return True
                return False

        if self.arr:
            if start >= self.arr[-1][1]:
                self.arr.append([start, end])
                return True
            return False
        self.arr.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
