class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                nums = []
                if r > 0:
                    nums.append(grid[r-1][c])
                if c > 0:
                    nums.append(grid[r][c-1])
                if nums:
                    grid[r][c] += min(nums)
        
        return grid[-1][-1]