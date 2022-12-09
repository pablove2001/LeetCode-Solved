class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        
        cmx= mx = cmn = mn = nums[0]
        for i in range(1, len(nums)):
            cmx = max(cmx+nums[i], nums[i])
            mx = max(mx, cmx)
            cmn = min(cmn+nums[i], nums[i])
            mn = min(mn, cmn)
        
        return max(mx, sum(nums)-mn)