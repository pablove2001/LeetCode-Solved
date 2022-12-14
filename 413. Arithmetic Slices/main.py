class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        d = defaultdict(int)
        count = 1
        dif = nums[0]-nums[1]

        for i in range(1, len(nums)-1):
            diff = nums[i]-nums[i+1]
            if dif == diff:
                count += 1
            else:
                if count >= 2:
                    d[count+1] += 1
                count = 1
                dif = diff 
        if count >= 2:
            d[count+1] += 1
        
        if not d:
            return 0

        l = []
        for k, v in d.items():
            l.append([k,v])
        l.sort()

        cal = 0
        idx = 0
        res = 0
        for i in range(1, l[-1][0]-1):
            cal += i
            if i+2 == l[idx][0]:
                res += cal*l[idx][1]
                idx += 1

        return res