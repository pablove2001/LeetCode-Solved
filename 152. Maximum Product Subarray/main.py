class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = pmx = pmn = nums[0]

        for i in range(1, len(nums)):
            cmx = max(pmx*nums[i], pmn*nums[i], nums[i])
            cmn = min(pmx*nums[i], pmn*nums[i], nums[i])
            pmx, pmn = cmx, cmn
            mx = max(mx, cmx)
        
        return mx