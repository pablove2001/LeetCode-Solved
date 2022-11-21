class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        r = c = 0
        ob = len(m)*len(m[0])
        cnt = 1
        res = [m[r][c]]
        m[r][c] = 'x'
        
        while cnt < ob:
            while c+1 < len(m[0]) and m[r][c+1] != 'x': # right
                c += 1
                cnt += 1
                res.append(m[r][c])
                m[r][c] = 'x'
                
            while r+1 < len(m) and m[r+1][c] != 'x': # bottom
                r += 1
                cnt += 1
                res.append(m[r][c])
                m[r][c] = 'x'
            
            while c-1 >= 0 and  m[r][c-1] != 'x': # left
                c -= 1
                cnt += 1
                res.append(m[r][c])
                m[r][c] = 'x'
                
            while r-1 >= 0 and m[r-1][c] != 'x': # up
                r -= 1
                cnt += 1
                res.append(m[r][c])
                m[r][c] = 'x'
        
        return res