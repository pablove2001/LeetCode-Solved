class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        return sorted(arr, key=keySort)

def keySort(num):
    return bin(num).count("1")