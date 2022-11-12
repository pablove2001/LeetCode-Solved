
def main(image, sr, sc, color):
    val = image[sr][sc]
    if val == color:
        return image
    
    return flood(image, sr, sc, color, val)
    

def flood(arr, r, c, color, val):
    if r >= len(arr) or c >= len(arr[0]) or r < 0 or c < 0 or arr[r][c] != val:
        return arr

    arr[r][c] = color

    arr = flood(arr, r+1, c, color, val) # top
    arr = flood(arr, r, c+1, color, val) # right
    arr = flood(arr, r-1, c, color, val) # bottom
    arr = flood(arr, r, c-1, color, val) # left

    return arr



image = [[0,0,0],[0,0,0]]
sr = 1
sc = 1
color = 0

print(main(image, sr, sc, color))