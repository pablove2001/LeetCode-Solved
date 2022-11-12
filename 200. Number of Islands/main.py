def main(grid):
    cnt = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                cnt += 1
                grid = flood(grid, r, c)
    
    return cnt

def flood(arr, r, c):
    if r >= len(arr) or c >= len(arr[0]) or r < 0 or c < 0 or arr[r][c] == "0":
        return arr
    arr[r][c] = "0"

    flood(arr, r+1, c) # top
    flood(arr, r, c+1) # right
    flood(arr, r-1, c) # bottom
    flood(arr, r, c-1) # left

    return arr


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(main(grid))