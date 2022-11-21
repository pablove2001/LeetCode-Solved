class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*len(t)
        stack = []
        
        for i, v in enumerate(t):
            while stack and stack[-1][1] < v:
                ind, nt = stack.pop()
                res[ind] = i-ind
                
            stack.append([i,v])
        
        return res