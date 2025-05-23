class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = {(row, col) : False for row in range(len(grid)) for col in range(len(grid[0]))}
        time = {(row, col) : float("inf") for row in range(len(grid)) for col in range(len(grid[0]))}

        minHeap = [[grid[0][0], [0, 0]]]
        time[(0, 0)] = grid[0][0]

        while len(minHeap) > 0:
            timeTaken, cur = heapq.heappop(minHeap)
            if visited[tuple(cur)] == True:
                continue
            
            visited[tuple(cur)] = True
            if cur[0] == len(grid) - 1 and cur[1] == len(grid[0]) - 1:
                return timeTaken

            for row, col in self.getNeighbors(grid, cur[0], cur[1]):
                if visited[(row, col)] == True:
                    continue
                timeRequired = max(grid[row][col], timeTaken)
                if timeRequired < time[(row, col)]:
                    time[(row, col)] = timeRequired
                    heapq.heappush(minHeap, [timeRequired, [row, col]])
        return -1
            
                
    def getNeighbors(self, grid, row, col):
        res = []
        rows = len(grid)
        cols = len(grid[0])

        if 0 <= row + 1 < rows and 0 <= col < cols:
            res.append([row + 1, col])
        if 0 <= row - 1 < rows and 0 <= col < cols:
            res.append([row - 1, col])
        if 0 <= row < rows and 0 <= col + 1 < cols:
            res.append([row, col + 1])
        if 0 <= row < rows and 0 <= col - 1 < cols:
            res.append([row, col - 1])
        
        return res



