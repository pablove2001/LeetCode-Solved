class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for n in nums:
            d[n] += n
        
        arr = []

        for k, v in d.items():
            arr.append([k,v])
        
        arr.sort()

        print(arr)

        if len(arr) == 1:
            return arr[0][1]
        
        if arr[0][0] != arr[1][0]-1:
            arr[1][1] += arr[0][1]
        
        if len(arr) == 2:
            return max(arr[-1][1], arr[-2][1])

        if arr[1][0] == arr[2][0]-1:
            arr[2][1] += arr[0][1]
        else:
            arr[2][1] += max(arr[1][1], arr[0][1])

        if len(arr) == 3:
            return max(arr[-1][1], arr[-2][1])
        
        for i in range(3, len(arr)):
            if arr[i-1][0] == arr[i][0]-1:
                arr[i][1] += max(arr[i-2][1], arr[i-3][1])
            else:
                arr[i][1] += max(arr[i-1][1], arr[i-2][1])
            
        print(arr)

        return max(arr[-1][1], arr[-2][1])