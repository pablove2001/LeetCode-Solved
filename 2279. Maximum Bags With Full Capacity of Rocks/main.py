class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], a: int) -> int:
        res = 0
        arr = []

        for i in range(len(capacity)):
            arr.append(capacity[i]-rocks[i])
        
        arr.sort()
        
        for i in range(len(arr)):
            if a < 1 or arr[i] - a > 0:
                return res
            a -= arr[i]
            res += 1

        return res