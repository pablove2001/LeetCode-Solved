class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(0, numRows-1):
            res.append([1])
            for j in range(i):
                res[i+1].append(res[i][j] + res[i][j+1])
            res[i+1].append(1)
            
        return res