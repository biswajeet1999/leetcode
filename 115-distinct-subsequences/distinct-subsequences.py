class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows = len(s) + 1
        cols = len(t) + 1

        prevRow = [0 for _ in range(cols)]
        curRow = [0 for _ in range(cols)]
        prevRow[0] = curRow[0] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                curRow[col] = prevRow[col]

                if s[row - 1] == t[col - 1]:
                    curRow[col] += prevRow[col - 1]
            prevRow = curRow[:]
        return prevRow[-1]