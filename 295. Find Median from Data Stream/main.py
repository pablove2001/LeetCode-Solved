class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # self.nums.append(num)
        # self.nums.sort()
        length = len(self.nums)

        if length == 0: 
            self.nums.append(num)
            return
        if num>self.nums[length-1]:
            self.nums.append(num)
            return
        for i in range(length):
             if num<=self.nums[i]:
                self.nums.insert(i,num)
                return
        return

    def findMedian(self) -> float:
        # print(self.nums)
        mid = (len(self.nums)-1)//2
        if len(self.nums) % 2 == 0:
            return (self.nums[mid]+self.nums[mid+1])/2
        else:
            return self.nums[mid]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()