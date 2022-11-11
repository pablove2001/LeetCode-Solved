class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        f = len(nums)
        while i < f:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                f-=1
            else:
                i+=1