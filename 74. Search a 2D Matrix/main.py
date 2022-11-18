class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = len(matrix)*len(matrix[0])-1
        if matrix[p1//len(matrix[0])][p1%len(matrix[0])] == target:
            return True
        if matrix[p2//len(matrix[0])][p2%len(matrix[0])] == target:
            return True
        while p2-p1 > 1:
            m = (p2-p1)//2+p1
            if  target > matrix[m//len(matrix[0])][m%len(matrix[0])]:
                p1 = m
            elif target < matrix[m//len(matrix[0])][m%len(matrix[0])]:
                p2 = m
            else:
                return True
        return False