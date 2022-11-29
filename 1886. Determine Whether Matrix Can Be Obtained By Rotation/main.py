class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target or return180(mat) == target:
            return True        
        
        arr = []
        for i in range(len(mat)):
            arr.append([])
            for j in range(len(mat)):
                arr[-1].append(mat[j][i])
            arr[-1] = arr[-1][::-1]
        
        if arr == target or return180(arr) == target:
            return True

def return180(mat):
    mat = mat[::-1]
    for i in range(len(mat)):
        mat[i] = mat[i][::-1]
    return mat