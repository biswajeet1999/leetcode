class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [None for _ in range(n)]
        self.solveNQueenUtil(n, 0, board, res)
        return res

    def solveNQueenUtil(self, n, curRow, board, res):
        if curRow == n:
            res.append(self.generateBoard(board))
            return
        
        for col in range(0, n):
            if self.safeToPlace(board, col, curRow, n):
                board[curRow] = col
                self.solveNQueenUtil(n, curRow + 1, board, res)
                board[curRow] = None
        
    def safeToPlace(self, board, col, row, n):
        # upward
        for idx in range(row - 1, -1, -1):
            if board[idx] == col:
                return False
        
        # left diag
        rowIdx = row - 1
        colIdx = col - 1
        while rowIdx >= 0 and colIdx >= 0:
            if board[rowIdx] == colIdx:
                return False
            rowIdx -= 1
            colIdx -= 1

        # right diag
        rowIdx = row - 1
        colIdx = col + 1
        while rowIdx >= 0 and colIdx < n:
            if board[rowIdx] == colIdx:
                return False
            rowIdx -= 1
            colIdx += 1
        return True

    def generateBoard(self, board):
        rows = cols = len(board)
        matrixBoard = []

        for row in range(rows):
            curRow = []
            for col in range(cols):
                if board[row] == col:
                    curRow.append("Q")
                else:
                    curRow.append(".")
            matrixBoard.append("".join(curRow))
        return matrixBoard