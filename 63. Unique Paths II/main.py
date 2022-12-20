class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        lenR = len(obstacleGrid)
        lenC = len(obstacleGrid[0])

        mp = [[0]*lenC for _ in range(lenR)]
        
        mp[0][0] = 1

        for r in range(lenR):
            for c in range(lenC):
                if obstacleGrid[r][c] != 1:
                    if r > 0:
                        mp[r][c] += mp[r-1][c]
                    if c > 0:
                        mp[r][c] += mp[r][c-1]

        return mp[-1][-1]