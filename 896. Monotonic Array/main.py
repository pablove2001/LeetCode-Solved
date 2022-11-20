class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        t1 = t2 = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                t2 = False
            if nums[i] > nums[i+1]:
                t1 = False
        return t1 or t2