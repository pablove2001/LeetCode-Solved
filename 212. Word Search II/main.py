class TrieNode:
    def __init__(self, char=None, letterToChild=None, word=None, prev=None):
        self.char = char
        self.letterToChild = letterToChild
        self.word = word
        self.prev = prev

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board[0]) == 0 or not words:
            return []

        def buildTrie(words: List[str]):
            root = TrieNode(char="/")
            for word in words:
                index = 0
                curNode = root
                while index < len(word):
                    char = word[index]
                    if not curNode.letterToChild:
                        curNode.letterToChild = {}
                    if char not in curNode.letterToChild:
                        childNode = TrieNode(char=char,letterToChild={},prev=curNode)
                        curNode.letterToChild[char] = childNode
                    else:
                        childNode = curNode.letterToChild[char]
                    
                    if index == len(word) - 1:
                        childNode.word = word
                        break

                    index += 1
                    curNode = childNode
            return root
        root = buildTrie(words)

        rows = len(board)
        cols = len(board[0])
        
        resultList = []
        def dfs(x,y,curNode:TrieNode):
            boardLetter = board[x][y]
            if boardLetter in curNode.letterToChild:
                board[x][y] = "*"
                nextNode = curNode.letterToChild[boardLetter]
                if nextNode.word:
                    resultList.append(nextNode.word)
                    nextNode.word = None
                    if len(nextNode.letterToChild) == 0:
                        parentNode = curNode
                        usedChar = nextNode.char
                        while len(parentNode.letterToChild) == 1:
                            del parentNode.letterToChild[usedChar]
                            usedChar = parentNode.char
                            if usedChar == "/":
                                break
                            parentNode = parentNode.prev                            

                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    adjX, adjY = x+dx, y+dy 
                    if 0 <= adjX < rows and 0 <= adjY < cols:
                        dfs(adjX,adjY,nextNode)
            board[x][y] = boardLetter
            return

        for x in range(rows):
            for y in range(cols):
                curNode = root 
                dfs(x,y,curNode)
        return resultList