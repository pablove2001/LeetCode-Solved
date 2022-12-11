class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                nums[i] = float('inf')
            else:
                ran = min(i + nums[i], len(nums))
                nums[i] = min(nums[i+1: ran+1])+1

        return nums[0]
