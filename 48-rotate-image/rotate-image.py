class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     for row in range(rows):
    #         for col in range(row + 1, cols):
    #             self.swap(matrix, row, col)
        
    #     left = 0
    #     right = cols - 1

    #     while left < right:
    #         for row in range(rows):
    #             temp = matrix[row][left]
    #             matrix[row][left] = matrix[row][right]
    #             matrix[row][right] = temp
    #         left += 1
    #         right -= 1

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.swapColumns(matrix)
    
    def transpose(self, matrix):
        rows = cols = len(matrix)

        for rowIdx in range(rows):
            for colIdx in range(rowIdx + 1, cols):
                self.swap(matrix, rowIdx, colIdx)

    def swapColumns(self, matrix):
        rows = cols = len(matrix)
        leftCol = 0
        rightCol = cols - 1

        while leftCol < rightCol:
            for row in range(0, rows):
                matrix[row][leftCol], matrix[row][rightCol] = matrix[row][rightCol], matrix[row][leftCol]
            leftCol += 1
            rightCol -= 1

    
    def swap(self, matrix, row, col):
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]