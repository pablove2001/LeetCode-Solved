class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        m = float('inf')
        s = {1}
        cambios = True
        roads.sort()
        print(roads)
        while cambios:
            cambios = False
            elim = []
            for i in range(len(roads)):
                if roads[i][0] in s or roads[i][1] in s:
                    s.add(roads[i][0])
                    s.add(roads[i][1])
                    m = min(m, roads[i][2])
                    elim.append(i)
                    cambios = True
            for i in elim[::-1]:
                roads.pop(i)
            
            print(roads)
        
        return m
