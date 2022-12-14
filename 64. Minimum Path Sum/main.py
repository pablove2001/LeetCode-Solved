class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = []
                if r > 0:
                    val.append(grid[r-1][c])
                if c > 0:
                    val.append(grid[r][c-1])
                if val:
                    grid[r][c] += min(val)
    
        return grid[-1][-1]