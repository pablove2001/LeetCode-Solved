class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(1, r):
            for j in range(c):
                inicio = max(0, j-1)
                fin = min(c-1, j+1)
                matrix[i][j] += min(matrix[i-1][inicio:fin+1])
        
        return min(matrix[-1])