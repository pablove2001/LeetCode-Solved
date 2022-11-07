class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dif = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if dif != arr[i+1] - arr[i]:
                return False
        return True
