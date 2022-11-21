class Solution:
    def kClosest(self, p: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        
        for x, y in p:
            arr.append([sqrt(x*x+y*y), [x, y]])
            
        arr.sort()
        
        return [a[1] for a in arr[:k]]