import copy

def main(board, words):
    output = []
    for w in words:
        if findLetter(board, w):
            output.append(w)
    return output

def findLetter(board, word):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if word[0] == board[y][x]:
                if findWord(copy.deepcopy(board), word, x, y, 1):
                    return True
    return False

def findWord(board, word, posX, posY, numL):
    board[posY][posX] = 0

    for x, y in ((0, -1), (1, 0), (0, 1), (-1, 0)): #top, right, bottom, left
        pass


board1 = []
words1 = []
print(main(board1, words1))