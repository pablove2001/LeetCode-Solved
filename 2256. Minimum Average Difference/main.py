class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        p1 = 0
        p2 = sum(nums)
        i = 0
        m = float('inf')
        le = len(nums)
        res = 0
        mw = 0
        while i < le:
            p1 += nums[i]
            p2 -= nums[i]
            if le-i-1 == 0:
                mw = p1//(i+1)
            else:
                mw = abs(p1//(i+1)-p2//(le-i-1))
            if mw < m:
                m = mw
                res = i
                
            i+=1
            

        return res