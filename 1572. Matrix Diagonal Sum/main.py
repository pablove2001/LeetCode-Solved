class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        suma = 0
        for i in range(len(mat)):
            j = len(mat)-1-i
            if i == j:
                suma += mat[i][i]
                continue
            suma += mat[i][i]
            suma += mat[i][j]
        return suma