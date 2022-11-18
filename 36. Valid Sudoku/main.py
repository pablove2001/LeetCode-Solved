class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dSet = {}

        for i in range(9):
            dSet['r'+str(i)] = set()
            dSet['c'+str(i)] = set()
            dSet['b'+str(i)] = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in dSet['r'+str(r)] or board[r][c] in dSet['c'+str(c)] or board[r][c] in dSet['b'+str(c//3+(r//3)*3)]:
                        return False
                    dSet['r'+str(r)].add(board[r][c])
                    dSet['c'+str(c)].add(board[r][c])
                    dSet['b'+str(c//3+(r//3)*3)].add(board[r][c])
        return True