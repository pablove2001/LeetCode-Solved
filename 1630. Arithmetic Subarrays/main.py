class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def correctAr(ar):
            ar.sort()
            d = ar[0]-ar[1]
            for i in range(len(ar)-1):
                if d != ar[i]-ar[i+1]:
                    return False
            return True
        
        res = []
        for i in range(len(l)):
            res.append(correctAr(nums[l[i]:r[i]+1]))
        return res