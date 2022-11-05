

def main(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def findOthers(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or 
            (r, c) in path):
            return False
        
        path.add((r, c))
        res = (findOthers(r + 1, c, i+1) or
            findOthers(r - 1, c, i+1) or
            findOthers(r, c + 1, i+1) or
            findOthers(r, c - 1, i+1))
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            if findOthers(r, c, 0): return True
    
    return False

board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCEDFC"
print(main(board1, word1))
            
