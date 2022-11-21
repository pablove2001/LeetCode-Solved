class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:    
        points.sort(key = lambda p: sqrt(p[0]*p[0]+p[1]*p[1]))
        
        return points[:k]