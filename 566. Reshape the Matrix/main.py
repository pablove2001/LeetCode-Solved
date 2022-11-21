class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        res = []
        i = 0
        for row in mat:
            for val in row:
                if i % c == 0:
                    res.append([])
                res[-1].append(val)
                i += 1
        
        return res
        