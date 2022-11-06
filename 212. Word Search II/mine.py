
def main(board, words):
    output = []
    for word in words:
        if find(board, word):
            output.append(word)
    return output

def find(board, word):
    for y in range(len(board)):
            for x in range(len(board[0])):
                if word[0] == board[y][x]:
                    if correctWord(copy2DList(board), list(word), x, y, 1):
                        return True
    return False

def correctWord(board, word, x, y, num):
    if len(word) == num:
        return True

    board[y][x] = 0

    #up
    if y > 0:
        if word[num] == board[y-1][x]:
            if correctWord(copy2DList(board), word, x, y-1, num+1):
                return True
    
    #right
    if x < len(board[0])-1:
        if word[num] == board[y][x+1]:
            if correctWord(copy2DList(board), word, x+1, y, num+1):
                return True
    
    #bottom
    if y < len(board)-1:
        if word[num] == board[y+1][x]:
            if correctWord(copy2DList(board), word, x, y+1, num+1):
                return True
    
    #left
    if x > 0:
        if word[num] == board[y][x-1]:
            if correctWord(copy2DList(board), word, x-1, y, num+1):
                return True
    
    #finally
    return False

def copy2DList(list):
    arr = []
    for i in range(len(list)):
        arr.append(list[i].copy())
    return arr


                        


board1 = [["a","b"],["c","d"]]
words1 = ["abcb"]
print(main(board1, words1))
#print(board1)