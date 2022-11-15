class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n]
        for r in range(1, m):
            arr = [1]
            for c in range(1, n):
                arr.append(arr[-1] + grid[r-1][c])
            grid.append(arr)
        return grid[-1][-1]