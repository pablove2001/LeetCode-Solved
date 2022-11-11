class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = 1
        res = 0
        while length <= len(arr):
            p1 = 0
            p2 = length
            while p2 <= len(arr):
                res += sum(arr[p1:p2])
                p1 += 1
                p2 += 1
            length += 2
        return res