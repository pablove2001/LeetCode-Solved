class Solution:      
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        for i in range(len(nums)):
            if target - nums[i] in nMap:
                return [nMap[target - nums[i]], i]
            nMap[nums[i]] = i