class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        topRow = 0
        bottomRow = len(matrix) - 1
        leftCol = 0
        rightCol = len(matrix[0]) - 1

        while topRow <= bottomRow and leftCol <= rightCol:
            self.traverseRow(matrix, topRow, leftCol, rightCol + 1, 1, res)
            self.traverseCol(matrix, rightCol, topRow + 1, bottomRow + 1, 1, res)
            if topRow != bottomRow:
                self.traverseRow(matrix, bottomRow, rightCol - 1, leftCol - 1, -1, res)
            if leftCol != rightCol:
                self.traverseCol(matrix, leftCol, bottomRow - 1, topRow,  -1, res)

            topRow += 1
            bottomRow -= 1
            leftCol += 1
            rightCol -= 1
        return res

    def traverseRow(self, matrix, rowIdx, fromCol, toCol, step, res):
        for colIdx in range(fromCol, toCol, step):
            res.append(matrix[rowIdx][colIdx])
    
    def traverseCol(self, matrix, colIdx, fromRow, toRow, step, res):
        for rowIdx in range(fromRow, toRow, step):
            res.append(matrix[rowIdx][colIdx])
        