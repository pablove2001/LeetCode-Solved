class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(rob1(nums[1:]), rob1(nums[:-1]))

def rob1(nums):
    if len(nums) <= 2:
        return max(nums)
    
    if len(nums) == 3:
        return max(nums[0]+nums[2], nums[1])
    
    nums[2] += nums[0]
    
    for i in range(3, len(nums)):
        nums[i] += max(nums[i-2], nums[i-3])

    return max(nums[-1], nums[-2])