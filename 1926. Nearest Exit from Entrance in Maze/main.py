class Solution:
    def nearestExit(self, m: List[List[str]], e: List[int]) -> int:
        visited = set()
        queue = []
        
        r, c = e
        queue.append((r,c,0))
        visited.add((r,c))
        
        while len(queue) > 0:
            r, c, step = queue.pop(0)
            
            if r-1 >= 0 and m[r-1][c] == '.' and (r-1, c) not in visited:
                if isExit(m, r-1, c):
                    return step + 1
                queue.append((r-1,c,step+1))
                visited.add((r-1,c))
            
            if c+1 < len(m[0]) and m[r][c+1] == '.' and (r, c+1) not in visited:
                if isExit(m, r, c+1):
                    return step + 1
                queue.append((r,c+1,step+1))
                visited.add((r,c+1))
                
            if r+1 < len(m) and m[r+1][c] == '.' and (r+1, c) not in visited:
                if isExit(m, r+1, c):
                    return step + 1
                queue.append((r+1,c,step+1))
                visited.add((r+1,c))
            
            if c-1 >= 0 and m[r][c-1] == '.' and (r, c-1) not in visited:
                if isExit(m, r, c-1):
                    return step + 1
                queue.append((r,c-1,step+1))
                visited.add((r,c-1))
        
        return -1

def isExit(m, r, c):
    if r-1 < 0 or c-1 < 0 or r+1>=len(m) or c+1>=len(m[0]):
        return True
    return False