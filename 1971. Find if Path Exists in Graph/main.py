class Solution:
    def validPath(self, n: int, edges: List[List[int]], so: int, de: int) -> bool:
        if so == de:
            return True
        
        edges.sort()
        s = set()
        change = True
        toPop = []

        for i in range(len(edges)):
            if so in edges[i] or de in edges[i]:
                s.add(edges[i][0])
                s.add(edges[i][1])
                edges.pop(i)
                break
        
        while change:
            toPop = []
            change = False
            for i in range(len(edges)):
                if edges[i][0] in s or edges[i][1] in s:
                    s.add(edges[i][0])
                    s.add(edges[i][1])
                    toPop.insert(0, i)
                    change = True
            
            for p in toPop:
                edges.pop(p)
            
            if so in s and de in s:
                return True
        
        return False